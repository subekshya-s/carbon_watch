"""
Analysis views for Carbon Watch.

Responsibility:
- Receive API requests
- Orchestrate the analysis workflow
- Persist results to the database
- Return serialized responses

All business logic lives in service modules and utility modules.
This view intentionally contains no domain logic.
"""

import logging

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from areaofintrest.models import District
from .models import AnalysisRun, CarbonEstimate
from .serializers import AnalysisRunSerializer
from .services.earth_engine import get_landcover_statistics
from .services.ai_service import generate_summary
from .calculations import calculate_landcover_percentages
from .carbon import estimate_carbon_stock

logger = logging.getLogger(__name__)


class TriggerAnalysisView(APIView):
    """
    Trigger a carbon analysis for a Nepal district.

    POST /api/districts/{district_id}/analyze/

    Workflow:
        1. Retrieve district from database
        2. Create AnalysisRun record (status: pending)
        3. Fetch ESA WorldCover land cover for 2020 and 2021
        4. Calculate land cover percentages (from 2021 data)
        5. Estimate carbon stock for both years
        6. Compute carbon change (2021 - 2020)
        7. Generate AI summary via Gemini
        8. Save CarbonEstimate to database
        9. Mark AnalysisRun as completed
        10. Return serialized response
    """

    def post(self, request, district_id):

        # ── Retrieve district ─────────────────────────────────────────
        try:
            district = District.objects.get(pk=district_id)
        except District.DoesNotExist:
            return Response(
                {"error": "District not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # ── Create analysis record ────────────────────────────────────
        analysis_run = AnalysisRun.objects.create(
            district=district,
            start_date="2020-01-01",
            end_date="2021-12-31",
            status="pending",
        )

        try:
            # ── Earth Engine: land cover for 2020 and 2021 ───────────
            landcover_2020 = get_landcover_statistics(district, year=2020)
            landcover_2021 = get_landcover_statistics(district, year=2021)

            # ── Land cover percentages (2021 baseline) ────────────────
            percentages = calculate_landcover_percentages(landcover_2021)

            # ── Carbon stock estimation ───────────────────────────────
            carbon_2020 = estimate_carbon_stock(landcover_2020)
            carbon_2021 = estimate_carbon_stock(landcover_2021)
            carbon_change = round(carbon_2021 - carbon_2020, 2)

            # ── AI summary ────────────────────────────────────────────
            ai_summary = generate_summary(
                district_name=district.name,
                carbon_2020=carbon_2020,
                carbon_2021=carbon_2021,
                carbon_change=carbon_change,
                percentages=percentages,
            )

            # ── Persist results ───────────────────────────────────────
            CarbonEstimate.objects.create(
                analysis_run=analysis_run,
                forest_area_pct=percentages["forest_area_pct"],
                cropland_area_pct=percentages["cropland_area_pct"],
                built_up_area_pct=percentages["built_up_area_pct"],
                other_area_pct=percentages["other_area_pct"],
                estimated_carbon_stock=carbon_2021,
                estimated_change=carbon_change,
                ai_summary=ai_summary,
            )

            analysis_run.status = "completed"
            analysis_run.save()

            logger.info(
                "Analysis completed for district=%s carbon_change=%s",
                district.name, carbon_change
            )

        except Exception:
            logger.exception(
                "Analysis failed for district=%s", district.name
            )
            analysis_run.status = "failed"
            analysis_run.save()
            return Response(
                {"error": "Analysis failed. Please try again."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        serializer = AnalysisRunSerializer(analysis_run)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnalysisResultView(RetrieveAPIView):
    """
    Retrieve a previously completed analysis result.

    GET /api/analyses/{id}/
    """
    queryset = AnalysisRun.objects.all()
    serializer_class = AnalysisRunSerializer

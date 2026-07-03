from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from areaofintrest.models import District
from .models import AnalysisRun, CarbonEstimate
from .serializers import AnalysisRunSerializer

class TriggerAnalysisView(APIView):
    def post(self, request, district_id):
        try:
            district = District.objects.get(pk=district_id)
        except District.DoesNotExist:
            return Response({'error': 'District not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create the analysis run
        analysis_run = AnalysisRun.objects.create(
            district=district,
            start_date='2020-01-01',
            end_date='2021-12-31',
            status='completed'
        )

        # Mock carbon estimate (placeholder until real EE pipeline)
        CarbonEstimate.objects.create(
            analysis_run=analysis_run,
            forest_area_pct=62.5,
            cropland_area_pct=18.3,
            built_up_area_pct=8.1,
            other_area_pct=11.1,
            estimated_carbon_stock=145230.5,
            estimated_change=-2340.2,
            ai_summary="Mock summary: This district shows moderate forest coverage with slight carbon loss between 2020 and 2021."
        )

        serializer = AnalysisRunSerializer(analysis_run)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnalysisResultView(RetrieveAPIView):
    queryset = AnalysisRun.objects.all()
    serializer_class = AnalysisRunSerializer

from rest_framework import serializers
from .models import AnalysisRun, CarbonEstimate

class CarbonEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonEstimate
        fields = ['forest_area_pct', 'cropland_area_pct', 'built_up_area_pct',
                  'other_area_pct', 'estimated_carbon_stock', 'estimated_change', 'ai_summary']

class AnalysisRunSerializer(serializers.ModelSerializer):
    carbon_estimate = CarbonEstimateSerializer(read_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)

    class Meta:
        model = AnalysisRun
        fields = ['id', 'district_name', 'start_date', 'end_date', 'status',
                  'created_at', 'carbon_estimate']

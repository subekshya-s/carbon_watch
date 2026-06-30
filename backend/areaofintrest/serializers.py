from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import District

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'province']

class DistrictGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = District
        geo_field = 'geometry'
        fields = ['id', 'name', 'province']

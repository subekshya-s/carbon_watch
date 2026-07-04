import json
import ee
from django.conf import settings

ee.Initialize(project=settings.EE_PROJECT)


def district_to_ee_geometry(district):
    """
    Convert a Django/PostGIS geometry into an Earth Engine Geometry.
    """

    # Convert GEOS geometry to GeoJSON
    geojson = json.loads(district.geometry.geojson)

    # Create Earth Engine geometry
    ee_geometry = ee.Geometry(geojson)

    return ee_geometry
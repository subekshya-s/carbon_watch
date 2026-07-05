import json
import ee

from django.conf import settings


# Initialize Earth Engine
try:
    ee.Initialize(project=settings.EE_PROJECT)
except Exception:
    ee.Authenticate()
    ee.Initialize(project=settings.EE_PROJECT)


def district_to_ee_geometry(district):
    """
    Convert a Django/PostGIS MultiPolygon into
    an Earth Engine Geometry.
    """

    geojson = json.loads(district.geometry.geojson)

    return ee.Geometry(geojson)


def get_landcover_image(district):
    """
    Returns the ESA WorldCover 2021 image
    clipped to the selected district.
    """

    geometry = district_to_ee_geometry(district)

    worldcover = (
        ee.ImageCollection("ESA/WorldCover/v200")
        .first()
    )

    clipped = worldcover.clip(geometry)

    return clipped
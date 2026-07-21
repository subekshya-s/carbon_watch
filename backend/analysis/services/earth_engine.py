"""
Earth Engine service for Carbon Watch.

Responsibilities:
- Earth Engine authentication and initialization
- PostGIS geometry to Earth Engine geometry conversion
- ESA WorldCover dataset loading
- Land cover statistics retrieval
"""

import json
import logging
import os
import tempfile

import ee
from django.conf import settings

logger = logging.getLogger(__name__)

_initialized = False

WORLDCOVER_DATASETS = {
    2020: "ESA/WorldCover/v100",
    2021: "ESA/WorldCover/v200",
}

CLASS_MAPPING = {
    "10": "tree_cover",
    "20": "shrubland",
    "30": "grassland",
    "40": "cropland",
    "50": "built_up",
    "60": "bare",
    "70": "snow_ice",
    "80": "water",
    "90": "wetland",
    "95": "mangroves",
    "100": "moss_lichen",
}


def _initialize_ee():
    """
    Initialize Earth Engine once using a service account.

    Supports two methods:
    1. EE_SERVICE_ACCOUNT_KEY_JSON env var (production/Render)
       - Full JSON key content stored as environment variable
    2. EE_SERVICE_ACCOUNT_KEY_PATH (local/Docker)
       - Path to local JSON key file
    """
    global _initialized
    if _initialized:
        return

    try:
        email = settings.EE_SERVICE_ACCOUNT_EMAIL

        # Method 1: JSON content from environment variable (Render)
        key_json = os.environ.get("EE_SERVICE_ACCOUNT_KEY_JSON")

        if key_json:
            # Write JSON to a temp file for the EE SDK
            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".json",
                delete=False
            ) as tmp:
                tmp.write(key_json)
                tmp_path = tmp.name

            credentials = ee.ServiceAccountCredentials(email, tmp_path)
            os.unlink(tmp_path)  # delete temp file immediately after use

        # Method 2: Local file path (Docker/development)
        else:
            key_path = settings.EE_SERVICE_ACCOUNT_KEY_PATH
            credentials = ee.ServiceAccountCredentials(email, key_path)

        ee.Initialize(credentials, project=settings.EE_PROJECT)
        logger.info("Earth Engine initialized successfully.")
        _initialized = True

    except Exception as exc:
        logger.exception("Failed to initialize Earth Engine.")
        raise RuntimeError(
            "Earth Engine is not configured correctly."
        ) from exc


def district_to_ee_geometry(district):
    """
    Convert a Django/PostGIS MultiPolygon district into
    an Earth Engine Geometry object.
    """
    geojson = json.loads(district.geometry.geojson)
    return ee.Geometry(geojson)


def _get_stats_for_image(image, geometry):
    """Run frequencyHistogram on a clipped image."""
    stats = image.reduceRegion(
        reducer=ee.Reducer.frequencyHistogram(),
        geometry=geometry,
        scale=10,
        maxPixels=1e10,
    )
    histogram = stats.get("Map").getInfo()
    return {
        CLASS_MAPPING.get(code, f"class_{code}"): area
        for code, area in histogram.items()
    }


def get_landcover_statistics(district, year):
    """
    Retrieve land cover pixel counts for a district for a given year.

    Args:
        district: District model instance.
        year: Integer year (2020 or 2021).

    Returns:
        dict mapping land cover class names to pixel counts.
    """
    _initialize_ee()

    if year not in WORLDCOVER_DATASETS:
        raise ValueError(
            f"Year {year} not supported. Supported: {list(WORLDCOVER_DATASETS.keys())}"
        )

    geometry = district_to_ee_geometry(district)
    dataset = WORLDCOVER_DATASETS[year]

    image = (
        ee.ImageCollection(dataset)
        .first()
        .clip(geometry)
    )

    landcover = _get_stats_for_image(image, geometry)

    logger.info(
        "Land cover statistics retrieved for district=%s year=%d classes=%d",
        district.name, year, len(landcover)
    )

    return landcover

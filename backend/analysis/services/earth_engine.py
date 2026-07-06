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

import ee
from django.conf import settings

logger = logging.getLogger(__name__)

# ESA WorldCover dataset versions by year
WORLDCOVER_DATASETS = {
    2020: "ESA/WorldCover/v100",
    2021: "ESA/WorldCover/v200",
}

# ESA WorldCover class codes to readable names
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

# Initialize Earth Engine on module load
try:
    ee.Initialize(project=settings.EE_PROJECT)
    logger.info("Earth Engine initialized successfully.")
except Exception:
    logger.warning("EE Initialize failed. Attempting authentication.")
    ee.Authenticate()
    ee.Initialize(project=settings.EE_PROJECT)


def district_to_ee_geometry(district):
    """
    Convert a Django/PostGIS MultiPolygon district into
    an Earth Engine Geometry object.

    Args:
        district: District model instance with PostGIS geometry field.

    Returns:
        ee.Geometry object.
    """
    geojson = json.loads(district.geometry.geojson)
    return ee.Geometry(geojson)


def get_landcover_statistics(district, year):
    """
    Retrieve land cover pixel counts for a district
    for a given year using ESA WorldCover.

    Args:
        district: District model instance.
        year: Integer year (2020 or 2021).

    Returns:
        dict mapping land cover class names to pixel counts.

    Raises:
        ValueError: If the requested year is not supported.
        Exception: If Earth Engine request fails.
    """
    if year not in WORLDCOVER_DATASETS:
        raise ValueError(
            f"Year {year} is not supported. "
            f"Supported years: {list(WORLDCOVER_DATASETS.keys())}"
        )

    geometry = district_to_ee_geometry(district)
    dataset = WORLDCOVER_DATASETS[year]

    image = (
        ee.ImageCollection(dataset)
        .first()
        .clip(geometry)
    )

    stats = image.reduceRegion(
        reducer=ee.Reducer.frequencyHistogram(),
        geometry=geometry,
        scale=10,
        maxPixels=1e10,
    )

    histogram = stats.get("Map").getInfo()

    landcover = {
        CLASS_MAPPING.get(code, f"class_{code}"): area
        for code, area in histogram.items()
    }

    logger.info(
        "Land cover statistics retrieved for district=%s year=%d classes=%d",
        district.name, year, len(landcover)
    )

    return landcover

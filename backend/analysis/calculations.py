"""
Land cover percentage calculations for Carbon Watch.

Responsibility:
- Convert raw land cover pixel counts into human-readable percentages.
"""

import logging

logger = logging.getLogger(__name__)


def calculate_landcover_percentages(landcover):
    """
    Convert land cover pixel counts into area percentages.

    Groups ESA WorldCover classes into four summary categories:
    - forest (tree_cover)
    - cropland
    - built_up
    - other (all remaining classes)

    Args:
        landcover: dict mapping class name strings to pixel counts.

    Returns:
        dict with keys:
            forest_area_pct, cropland_area_pct,
            built_up_area_pct, other_area_pct
        All values are rounded to 2 decimal places.
    """
    total_area = sum(landcover.values())

    if total_area == 0:
        logger.warning("Total land cover area is 0. Returning zero percentages.")
        return {
            "forest_area_pct": 0.0,
            "cropland_area_pct": 0.0,
            "built_up_area_pct": 0.0,
            "other_area_pct": 0.0,
        }

    forest = landcover.get("tree_cover", 0)
    cropland = landcover.get("cropland", 0)
    built_up = landcover.get("built_up", 0)
    other = total_area - forest - cropland - built_up

    percentages = {
        "forest_area_pct": round(forest / total_area * 100, 2),
        "cropland_area_pct": round(cropland / total_area * 100, 2),
        "built_up_area_pct": round(built_up / total_area * 100, 2),
        "other_area_pct": round(other / total_area * 100, 2),
    }

    logger.debug("Land cover percentages calculated: %s", percentages)
    return percentages

"""
Carbon estimation module for Carbon Watch.

Responsibility:
- Define biomass-to-carbon coefficients per land cover class.
- Estimate total carbon stock from land cover pixel counts.

Note:
    These coefficients are placeholder values for Carbon Watch v1.
    They are approximate proxies based on general literature and are
    NOT IPCC-certified. They should not be used for official MRV
    (Measurement, Reporting, Verification) purposes.

    Future v2 improvement: replace with IPCC Tier 1 default factors
    or literature-based values validated against NASA GEDI LiDAR
    biomass data.

    Units: tonnes of Carbon per hectare (tC/ha).
    Pixel area at 10m resolution = 100 m² = 0.01 ha.
"""

import logging

logger = logging.getLogger(__name__)

# Biomass-to-carbon coefficients (tC/ha) per ESA WorldCover class
CARBON_FACTORS = {
    "tree_cover": 150,
    "shrubland": 35,
    "grassland": 12,
    "cropland": 8,
    "built_up": 0,
    "bare": 1,
    "water": 0,
    "snow_ice": 0,
    "wetland": 20,
    "mangroves": 180,
    "moss_lichen": 5,
}

# Pixel area conversion: 10m resolution → hectares
PIXEL_AREA_HA = 0.01


def estimate_carbon_stock(landcover):
    """
    Estimate total carbon stock from land cover pixel counts.

    Calculation:
        carbon = sum(pixel_count × pixel_area_ha × carbon_factor)

    Args:
        landcover: dict mapping land cover class names to pixel counts.

    Returns:
        Total estimated carbon stock in tonnes C (rounded to 2 dp).
    """
    total_carbon = sum(
        pixel_count * PIXEL_AREA_HA * CARBON_FACTORS.get(lc_class, 0)
        for lc_class, pixel_count in landcover.items()
    )

    result = round(total_carbon, 2)
    logger.debug("Estimated carbon stock: %s tC", result)
    return result

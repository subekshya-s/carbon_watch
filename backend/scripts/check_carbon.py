import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from areaofintrest.models import District

from analysis.services.earth_engine import (
    get_landcover_statistics,
)

from analysis.carbon import estimate_carbon_stock


district = District.objects.get(name="Bhojpur")

landcover = get_landcover_statistics(district)

carbon = estimate_carbon_stock(landcover)

print("\nLand Cover")
print("----------------------")
print(landcover)

print("\nEstimated Carbon")
print("----------------------")
print(carbon)
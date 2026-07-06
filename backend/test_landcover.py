import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from areaofintrest.models import District
from analysis.services.earth_engine import (
    get_landcover_statistics,
    calculate_landcover_percentages,
)

district = District.objects.get(name="Bhojpur")

landcover = get_landcover_statistics(district)

percentages = calculate_landcover_percentages(landcover)

print("\nLand Cover Areas")
print("----------------")
print(landcover)

print("\nPercentages")
print("----------------")
print(percentages)
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from areaofintrest.models import District
from analysis.services.earth_engine import district_to_ee_geometry

district = District.objects.first()

print("District:", district.name)

ee_geom = district_to_ee_geometry(district)

print("Earth Engine Geometry created successfully!")

print(ee_geom.getInfo()["type"])
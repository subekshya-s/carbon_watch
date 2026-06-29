import json
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from areaofintrest.models import District

class Command(BaseCommand):
    help = "Load Nepal districts from GeoJSON into the database"

    def handle(self, *args, **kwargs):
        geojson_path = os.path.join(settings.BASE_DIR, "..", "data", "Nepal_District_Geojson.geojson")
        geojson_path = os.path.abspath(geojson_path)

        self.stdout.write(f"Looking for file at: {geojson_path}")

        with open(geojson_path) as f:
            data = json.load(f)

        created_count = 0
        updated_count = 0

        for feature in data["features"]:
            name = feature["properties"]["DISTRICT"]
            province = feature["properties"]["PR_NAME"]
            geom = GEOSGeometry(json.dumps(feature["geometry"]))

            obj, created = District.objects.update_or_create(
                name=name,
                defaults={"province": province, "geometry": geom}
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"Done. Created: {created_count}, Updated: {updated_count}, Total: {District.objects.count()}"
        ))

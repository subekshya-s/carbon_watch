from pathlib import Path
import json

from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand

from areaofintrest.models import District


class Command(BaseCommand):
    help = "Load Nepal districts from GeoJSON"

    def handle(self, *args, **options):
        geojson_path = Path(settings.BASE_DIR) / "data" / "Nepal_District_Geojson.geojson"

        self.stdout.write(f"Looking for file at: {geojson_path}")

        if not geojson_path.exists():
            self.stderr.write(
                self.style.ERROR(f"GeoJSON file not found: {geojson_path}")
            )
            return

        with open(geojson_path, encoding="utf-8") as f:
            data = json.load(f)

        for feature in data["features"]:
            properties = feature["properties"]

            district_name = (
                properties.get("DISTRICT")
                or properties.get("district")
                or properties.get("name")
            )

            geometry = GEOSGeometry(json.dumps(feature["geometry"]))

            District.objects.update_or_create(
                name=district_name,
                defaults={"geometry": geometry},
            )

        self.stdout.write(
            self.style.SUCCESS("Districts loaded successfully!")
        )

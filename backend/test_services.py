import os
import django

# Tell Python where Django settings are
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Start Django
django.setup()

from analysis.services import earth_engine

print("✅ Earth Engine service loaded successfully!")
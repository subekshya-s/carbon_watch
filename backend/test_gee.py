import ee

ee.Initialize(project="gisprojects-487408")

print("✅ Earth Engine initialized successfully!")

image = ee.Image("ESA/WorldCover/v100/2020")

print("Image loaded successfully!")
print(image.getInfo()["id"])
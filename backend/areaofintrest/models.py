from django.contrib.gis.db import models as gis_models
from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    province = models.CharField(max_length=100)
    geometry = gis_models.MultiPolygonField()

    def __str__(self):
        return self.name

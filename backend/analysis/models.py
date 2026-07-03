from django.db import models
from areaofintrest.models import District

class AnalysisRun(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='analyses')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.district.name} ({self.start_date} to {self.end_date})"


class CarbonEstimate(models.Model):
    analysis_run = models.OneToOneField(AnalysisRun, on_delete=models.CASCADE, related_name='carbon_estimate')
    forest_area_pct = models.FloatField(default=0)
    cropland_area_pct = models.FloatField(default=0)
    built_up_area_pct = models.FloatField(default=0)
    other_area_pct = models.FloatField(default=0)
    estimated_carbon_stock = models.FloatField(help_text="tonnes C", default=0)
    estimated_change = models.FloatField(help_text="tonnes C change from 2020 to 2021", default=0)
    ai_summary = models.TextField(blank=True)

    def __str__(self):
        return f"Carbon estimate for {self.analysis_run}"

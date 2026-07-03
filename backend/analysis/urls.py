from django.urls import path
from .views import TriggerAnalysisView, AnalysisResultView

urlpatterns = [
    path('districts/<int:district_id>/analyze/', TriggerAnalysisView.as_view(), name='trigger-analysis'),
    path('analyses/<int:pk>/', AnalysisResultView.as_view(), name='analysis-result'),
]

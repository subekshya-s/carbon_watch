from django.urls import path
from .views import DistrictListView, DistrictDetailView

urlpatterns = [
    path('districts/', DistrictListView.as_view(), name='district-list'),
    path('districts/<int:pk>/', DistrictDetailView.as_view(), name='district-detail'),
]

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import District
from .serializers import DistrictSerializer, DistrictGeoSerializer

class DistrictListView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class DistrictDetailView(RetrieveAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictGeoSerializer

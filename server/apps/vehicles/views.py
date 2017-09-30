import json
from rest_framework import status, viewsets, mixins
# from rest_framework.response import Response
# from rest_framework.decorators import detail_route, list_route, api_view

from .models import *
from .serializers import *


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = VehicleSession.objects.all()
    serializer_class = VehicleSerializer

class VehicleSessionViewSet(viewsets.ModelViewSet):
    queryset = VehicleSession.objects.all()
    serializer_class = VehicleSessionSerializer

class VehicleSessionMetricViewSet(viewsets.ModelViewSet):
    queryset = VehicleSessionMetric.objects.all()
    serializer_class = VehicleSessionMetricSerializer

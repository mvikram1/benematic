import json
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route, api_view

from .models import *
from .serializers import *


class Vehicle(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VehicleSession.objects.all()
    serializer_class = Vehicle

class VehicleSessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VehicleSession.objects.all()
    serializer_class = VehicleSession

class VehicleSessionMetricViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VehicleSessionMetric.objects.all()
    serializer_class = VehicleSessionMetric

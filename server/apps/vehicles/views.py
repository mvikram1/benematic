import json
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
# from rest_framework.decorators import detail_route, list_route, api_view

from .models import *
from .serializers import *


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleSessionViewSet(viewsets.ModelViewSet):
    queryset = VehicleSession.objects.all()
    serializer_class = VehicleSessionSerializer
    model = VehicleSession

    def create(self, request):
        data = json.loads(request.body.decode('utf-8'))
        vin = data.get('vin')
        try:
            vehicle = Vehicle.objects.get(vin=vin)
        except:
            vehicle = Vehicle.objects.create(vin=vin)
        session = VehicleSession.objects.create(vehicle=vehicle)
        return Response({'id':session.id}, status=status.HTTP_200_OK)

    def delete(self, request):
        VehicleSession.objects.update(id=request.POST.get('id'))

class VehicleSessionMetricViewSet(viewsets.ModelViewSet):
    queryset = VehicleSessionMetric.objects.all()
    serializer_class = VehicleSessionMetricSerializer

    def create(self, request):
        data = json.loads(request.body.decode('utf-8'))
        try:
            metric = VehicleSessionMetric.objects.create(**data)
            return Response({'id': metric.id}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ExcessMetricViewSet(viewsets.ModelViewSet):
    queryset = VehicleSessionMetric.objects.filter(metric__in=['hard_turn', 'hard_acceleration', 'hard_brake', 'no_driver_seatbelt', 'no_passenger_seatbelt'])
    serializer_class = VehicleSessionMetricSerializer

    def create(self, request, *args, **kwargs):
        raise NotImplementedError()

    def update(self, request, *args, **kwargs):
        raise NotImplementedError()

    def delete(self, request, *args, **kwargs):
        raise NotImplementedError()


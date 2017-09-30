from rest_framework import serializers
from .models import *

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Vehicle:
        model = Vehicle
        fields = ('vin',)
        read_only_fields = ('id',)


class VehicleSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleSession
        fields = ('vehicle', 'created_at', 'modified_at',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleSessionMetric
        fields = ('vehicle_session', 'metric', 'value',)



from rest_framework import serializers
from .models import *

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('vin',)
        read_only_fields = ('id',)


class VehicleSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleSession
        fields = ('vehicle_id', 'created_at', 'modified_at',)


class VehicleSessionMetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleSessionMetric
        fields = ('vehicle_session_id', 'metric', 'value',)



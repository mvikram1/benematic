from rest_framework import serializers
from .models import State, Zipcode


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ('code', 'name', )
        read_only_fields = ('code', 'name', )


class ZipcodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zipcode
        fields = ('code', 'city', 'state', )
        read_only_fields = ('code', 'city', 'state',)
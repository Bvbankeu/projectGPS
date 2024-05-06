from rest_framework import serializers
from position.models import *

class GpsModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GpsModule
        fields = ['id', 'battery', 'simNumber', 'idEnfant']


class GpsCoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    gpsModule = serializers.PrimaryKeyRelatedField(queryset=GpsModule.objects.all())
    
    class Meta:
        model = GpsCoordinates
        fields = ['date', 'gpsModule', 'longitude', 'latitude']
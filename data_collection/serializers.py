from data_collection.models import *
from rest_framework import serializers

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('idsite', 'site', 'active')


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('idworker', 'worker', 'workertype', 'active')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    sites = SiteSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('location', 'idlocation', 'sites', 'active')

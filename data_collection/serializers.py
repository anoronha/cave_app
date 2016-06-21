from data_collection.models import *
from rest_framework import serializers

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('idsite', 'site', 'sitetype', 'location', 'active')

class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
        fields = ('idworker', 'workername', 'workertype','affiliation','jobtitle','active','email','phonenumber')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    fk_Site_Location = SiteSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('location', 'idlocation', 'fk_Site_Location', 'active')

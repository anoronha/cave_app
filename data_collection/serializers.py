from data_collection.models import *
from rest_framework import serializers

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('idsite', 'site','sitetype', 'active')

    # def get_queryset(self):
    #     queryset = Site.objects.all()
    #     location = self.request.query_params.get('location', None)
    #     print(location)
    #     if location is not None:
    #         queryset = queryset.filter(location=location).filter(active=1)
    #     return queryset

class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
        fields = ('idworker', 'workername', 'workertype','affiliation','jobtitle','active','email','phonenumber')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    fk_Site_Location = SiteSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('location', 'idlocation', 'fk_Site_Location', 'active')

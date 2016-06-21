from rest_framework import viewsets
from data_collection.models import *
from data_collection.serializers import *

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer

    def get_queryset(self):
        queryset = Site.objects.all()
        is_active = self.request.query_params.get('is_active', None)
        location = self.request.query_params.get('location', None)
        filter_out = self.request.query_params.get('filter_out', None)
        if location is not None:
            queryset = queryset.filter(location=location)
        if is_active is not None:
            queryset = queryset.filter(active=is_active)
        if filter_out is not None:
            queryset = queryset.exclude(sitetype=filter_out)

        return queryset

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

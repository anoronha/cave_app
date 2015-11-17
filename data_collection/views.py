from django.shortcuts import render
from data_collection.models import *
from django.shortcuts import get_object_or_404

def new_fieldtrip(request):
    location_all = Location.objects.exclude(active=0)
    site_all = Site.objects.exclude(active=0).exclude(sitetype='cave room')
    worker_all = Worker.objects.exclude(active=0).exclude(workertype='Lab').order_by('-worker')
    # tmp = get_object_or_404(Fieldtrip, pk=idfieldtrip)
    return render(request, 'new_fieldtrip.html', {
        'location_all': location_all,
        'site_all': site_all,
        'worker_all': worker_all,
    })

def tmp(request):
    location_all = Location.objects.exclude(active=0)
    return render(request, 'tmp.html', {
        'location_all': location_all,
    })

#def new_FieldTrip():


def index(request):
    return render(request, 'index.html')

def enter_tmp(request, location):
    return HttpResponse("You're making a new field trip to %s." % location)

def results(request, location):
    return render(request, 'results.html')

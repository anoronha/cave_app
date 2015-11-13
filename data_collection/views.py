from django.shortcuts import render
from data_collection.models import *

# Create your views here.

def enter_data(request):
    location_all = Location.objects.exclude(active=0)
    site_all = Site.objects.exclude(active=0).exclude(sitetype='cave room')
    worker_all = Worker.objects.exclude(active=0).exclude(workertype='Lab').order_by('-worker')
    return render(request, 'enter_data.html', {
        'location_all': location_all,
        'site_all': site_all,
        'worker_all': worker_all,
    })

def index(request):
    return render(request, 'index.html')

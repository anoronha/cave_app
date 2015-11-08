from django.shortcuts import render
from data_collection.models import *

# Create your views here.

def enter_data(request):
    loc = Location.objects.all()
    sit = Site.objects.all()
    return render(request, 'enter_data.html', {
        'loc': loc,
        'sit': sit,
    })

def index(request):
    return render(request, 'index.html')
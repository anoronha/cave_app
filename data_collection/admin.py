from django.contrib import admin
from .models import Location, Site, Sitetype, Worker, Bottlesize, Bottletype
# Register your models here.

admin.site.register(Location)
admin.site.register(Site)
admin.site.register(Sitetype)
admin.site.register(Worker)
admin.site.register(Bottlesize)
admin.site.register(Bottletype)

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from data_collection import api

router = routers.DefaultRouter()
router.register(r'locations', api.LocationViewSet)
router.register(r'sites', api.SiteViewSet)
router.register(r'workers', api.WorkerViewSet)

urlpatterns = [
    url(r'^$','data_collection.views.index',name='home'),
    url(r'^new-fieldtrip/$','data_collection.views.new_fieldtrip', name = 'new-fieldtrip'),
    url(r'^enter-site-data/$','data_collection.views.enter_site_data', name = 'enter-site-data'),
    url(r'^download-data/$',TemplateView.as_view(template_name='download_data.html'), name = 'download-data'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace="api")),
    url(r'^alk/$','data_collection.views.alk', name = 'alk'),
    url(r'^new-fieldtrip/field-instruments/$','data_collection.views.field_instruments', name = 'field_instruments'),
    url(r'^enter-data/$','data_collection.views.enter_data', name = 'enter_data'),
    url(r'^permission-holder/$','data_collection.views.permission_holder', name = 'permission_holder'),
    url(r'^success/$','data_collection.views.success', name = 'success'),
    url(r'^people/$','data_collection.views.modify_people', name = 'people'),
    # url(r'^sites/$','data_collection.views.modify_sites', name = 'people'),
    # url(r'^worker/$','data_collection.views.worker', name = 'worker'),
    # url(r'^lines/$','data_collection.views.lines', name = 'lines'),
    # url(r'^alk/$','data_collection.views.samples_collected', name = 'samples-collected'),
]

print(urlpatterns)

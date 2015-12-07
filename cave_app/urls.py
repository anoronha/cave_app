from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from data_collection import api

router = routers.DefaultRouter()
router.register(r'locations', api.LocationViewSet)
router.register(r'sites', api.SiteViewSet)

urlpatterns = [
    url(r'^$','data_collection.views.index',name='home'),
    url(r'^new-fieldtrip/$','data_collection.views.new_fieldtrip', name = 'new-fieldtrip'),
    url(r'^new-fieldtrip/select-sites/$','data_collection.views.new_fieldtrip_sites', name = 'new-fieldtrip-sites'),
    url(r'^enter-site-data/$','data_collection.views.enter_site_data', name = 'enter-site-data'),
    url(r'^download-data/$',TemplateView.as_view(template_name='download_data.html'), name = 'download-data'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace="api")),
    url(r'^alk/$','data_collection.views.alk', name = 'alk'),
    url(r'^new-fieldtrip/field-instruments/$','data_collection.views.field_instruments', name = 'field_instruments'),
    # url(r'^alk/$','data_collection.views.samples_collected', name = 'samples-collected'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.new_FieldTrip, name='vote'),
]

print(urlpatterns)

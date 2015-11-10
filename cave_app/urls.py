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
    url(r'^enter-data/$','data_collection.views.enter_data', name = 'enter-data'),
    url(r'^download-data/$',TemplateView.as_view(template_name='download_data.html'), name = 'download-data'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace="api")),
]

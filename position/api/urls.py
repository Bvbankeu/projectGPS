from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from position.api.views import *

router = routers.DefaultRouter()
router.register(r'gpsModule', GpsModuleViewSet)
router.register(r'gpsCoordinates', GpsCoordinatesViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eboutique.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
  #   url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)
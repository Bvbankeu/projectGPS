"""
URL configuration for heldisGPS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from position.api.views import *
from translate.views import *

router = routers.DefaultRouter()
router.register(r'gpsModule', GpsModuleViewSet, basename='gpsModule')
router.register(r'gpsCoordinates', GpsCoordinatesViewSet, basename='gpsCoordinates')




###urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eboutique.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^api/', include(router.urls)),
  #   url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
#)
###
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('translate/login/', login, name='login'),
    path('translate/onlineGPS/', onlineGPS, name='onlineGPS'),
    path('translate/reste/', reste, name='reste'),
    path('translate/status/', status, name='status'),
    path('translate/offlineGPS/', offlineGPS, name='offlineGPS'),
    path('translate/offlineWifi/', offlineWifi, name='offlineWifi'),
    path('translate/wifiPositioning/', wifiPositioning, name='wifiPositioning'),
    path('translate/updateTime/', updateTime, name='updateTime'),
    path('translate/setParams/', setParams, name='setParams'),
    path('translate/offStatus/', offStatus, name='offStatus'),
    path('translate/setStatus/', setStatus, name='setStatus'),
]

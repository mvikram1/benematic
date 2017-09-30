"""
GM URL Configuration
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from apps.pages.views import home
from apps.vehicles.views import *
from apps.locations.views import *

router = routers.DefaultRouter()
router.register(r'vehicle', VehicleViewSet)
router.register(r'session', VehicleSessionViewSet)
router.register(r'metric', VehicleSessionMetricViewSet)
router.register(r'states', StateViewSet)

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^loc/', include('apps.locations.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]


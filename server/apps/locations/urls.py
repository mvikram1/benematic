from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', StateListView.as_view(), name='state.list'),
    url(r'^(?P<pk>[A-Z]{2})/$', StateDetailView.as_view(), name='state.detail'),
]
from django.conf.urls import patterns, url

urlpatterns = patterns('sven.apps.sensors.views',
    url(r'^$', 'index', name='index'),
    url(r'^index$', 'index', name='index'),
)

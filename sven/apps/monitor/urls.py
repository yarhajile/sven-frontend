from django.conf.urls import patterns, url

urlpatterns = patterns( 'sven.apps.monitor.views',
    url( r'^$', 'index', name='index'),
    url( r'^index$', 'index', name='index'),

    url( r'^locationGroups$', 'locationGroups', name='locationGroups'),

    url( r'^locationGroup/(?P<id>\d+)/$', 'locationGroup', name='locationGroup'),

    url( r'^location/(?P<id>\d+)/$', 'location', name='location'),
    url( r'^location/new/$', 'location', name='locationNew'),

#    url( r'^device/new/(?P<locationId>\d+)/$', 'device', name='deviceNew'),
    url( r'^device/(?P<id>\d+)/$', 'device', name='device'),
    url( r'^device/new/$', 'device', name='deviceNew'),

    url( r'^ajaxListLocationGroups$', 'ajaxListLocationGroups', name='ajaxListLocationGroups'),
    url( r'^ajaxListLocations$', 'ajaxListLocations', name='ajaxListLocations'),
    url( r'^ajaxListDevices$', 'ajaxListDevices', name='ajaxListDevices'),

    url( r'^ajaxUpdateLocationGroup$', 'ajaxUpdateLocationGroup', name='ajaxUpdateLocationGroup'),
    url( r'^ajaxUpdateLocation$', 'ajaxUpdateLocation', name='ajaxUpdateLocation'),
    url( r'^ajaxUpdateDevice$', 'ajaxUpdateDevice', name='ajaxUpdateDevice'),
    url( r'^ajaxUpdateDeviceAction', 'ajaxUpdateDeviceAction', name='ajaxUpdateDeviceAction'),

    url( r'^ajaxInputMatrix', 'ajaxInputMatrix', name='ajaxInputMatrix'),
    url( r'^ajaxLoadWidgets', 'ajaxLoadWidgets', name='ajaxLoadWidgets'),
)

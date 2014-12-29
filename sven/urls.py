from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns( '',
    url( r'^admin/',            include( admin.site.urls ) ),

    url( r'^dashboard/',        include( 'sven.apps.dashboard.urls',        namespace = 'dashboard' ) ),
    url( r'^configuration/',    include( 'sven.apps.configuration.urls',    namespace = 'configuration' ) ),
    url( r'^monitor/',          include( 'sven.apps.monitor.urls',          namespace = 'monitor' ) ),

    url( r'^activity/',         include( 'sven.apps.activity.urls',         namespace = 'activity' ) ),
    url( r'^sensors/',          include( 'sven.apps.sensors.urls',          namespace = 'sensors' ) ),
)

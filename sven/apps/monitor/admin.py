from django.contrib import admin
from sven.apps.monitor.models import *

# Register your models here.
class SvenAdmin( admin.ModelAdmin ):

    """
    Base class to add default ordering
    """

    def __init__( self, model, admin_site ):
        super( SvenAdmin, self ).__init__( model, admin_site )

        self.ordering = ['name']


    class Meta:
        abstract = True


class SvenHasActiveAdmin( SvenAdmin ):

    """
    Base class for adding active / inactive flagging actions list and list_display fields
    """

    def __init__( self, model, admin_site ):
        super( SvenHasActiveAdmin, self ).__init__( model, admin_site )

        self.actions         = ['mark_selected_as_active', 'mark_selected_as_inactive']
        self.list_display    = [ 'id', 'active', 'name', 'description' ]


    class Meta:
        abstract = True


    def mark_selected_as_active( self, request, queryset ):
        queryset.update( active = True )


    def mark_selected_as_inactive( self, request, queryset ):
        queryset.update( active = False )


    def list_display_extend( self, parameters ):
        self.list_display.extend( parameters )
        self.list_display.extend( [ 'created', 'updated' ] )

#
# Location_Groups model
#
class LocationGroupsAdmin( SvenHasActiveAdmin ):

    """
    All columns handled by parent
    """


#
# Locations model
#
class LocationsAdmin( SvenHasActiveAdmin ):

    """
    Add columns for 'location_group'
    """

    def __init__( self, model, admin_site ):
        super( LocationsAdmin, self ).__init__( model, admin_site )

        self.list_display_extend( [ 'location_group' ] )


#
# Devices
#
class DevicesAdmin( SvenHasActiveAdmin ):

    """
    Add columns for 'current_value'
    """

    def __init__( self, model, admin_site ):
        super( DevicesAdmin, self ).__init__( model, admin_site )

        self.list_display_extend( [ 'current_value' ] )


#
# Location_Devices model
#
class LocationDevicesAdmin( SvenHasActiveAdmin ):

    """
    Add columns for 'device' and 'location'
    """

    def __init__( self, model, admin_site ):
        super( LocationDevicesAdmin, self ).__init__( model, admin_site )

        self.list_display_extend( [ 'device', 'location' ] )


#
# Device_Type_Parameters model
#
class DeviceParametersAdmin( SvenHasActiveAdmin ):

    """
    Add columns for 'parameter' and 'value'
    """

    def __init__( self, model, admin_site ):
        super( DeviceParametersAdmin, self ).__init__( model, admin_site )

        self.list_display_extend( [ 'parameter', 'value' ] )


#
# History model
#
class HistoryAdmin( SvenAdmin ):

    """
    Add columns for 'id', 'key', 'value', 'created' and 'updated'
    """

    def __init__( self, model, admin_site ):
        super( HistoryAdmin, self ).__init__( model, admin_site )

        self.ordering        = [ 'id' ]
        self.list_display    = [ 'id', 'key', 'value', 'created', 'updated' ]


#
# Register the models with their admin class
#
admin.site.register( Location_Group, LocationGroupsAdmin )
admin.site.register( Location, LocationsAdmin )
admin.site.register( Device, DevicesAdmin )
admin.site.register( Location_Device, LocationDevicesAdmin )
admin.site.register( Device_Parameter, DeviceParametersAdmin )
admin.site.register( History, HistoryAdmin )

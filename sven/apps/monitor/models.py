from django.db import models

class SvenAbstract( models.Model ):
    created = models.DateTimeField( auto_now_add = True )
    updated = models.DateTimeField( auto_now = True, auto_now_add = True )

    class Meta:
        abstract    = True


class SvenAbstractNDA( SvenAbstract ):

    """
    Create Name, Description and Active fields
    """
    name            = models.CharField( max_length = 255, null = True, blank = True )
    description     = models.TextField( null = True, blank = True )
    active          = models.BooleanField( default = True )

    class Meta:
        abstract    = True


    def __str__( self ):
        return self.name


class Location_Group( SvenAbstractNDA ):
    pass


class Location( SvenAbstractNDA ):
    location_group      = models.ForeignKey( Location_Group )


class Device( SvenAbstractNDA ):
    current_value       = models.CharField( max_length = 255 )
    update_trigger      = models.BooleanField( default = False )

    def save( self, *args, **kwargs ):
        self.update_trigger = True

        super( Device, self ).save( *args, **kwargs )


class Device_Parameter( SvenAbstract ):
    device      = models.ForeignKey( Device )
    parameter   = models.CharField( max_length = 64 )
    value       = models.CharField( max_length = 64 )


# Create 1:many relationships on the arm_status.
# This allows actions to exist in one or more arming states.
class Arm_Status( models.Model ):
    status = models.CharField( max_length = 255 )


class Arm_Status_Device( models.Model ):
    device = models.ForeignKey( Device )
    arm_status = models.ForeignKey( Arm_Status )


class Arm_Status_Location( models.Model ):
    location = models.ForeignKey( Location )
    arm_status = models.ForeignKey( Arm_Status )


class Arm_Status_Location_Group( models.Model ):
    location_group = models.ForeignKey( Location_Group )
    arm_status = models.ForeignKey( Arm_Status )


class Event( SvenAbstract ):
    message = models.TextField( )
    viewed  = models.BooleanField( default = False )


class Location_Device( SvenAbstractNDA ):
    device          = models.ForeignKey( Device )
    location        = models.ForeignKey( Location )


class History( SvenAbstract ):
    key     = models.CharField( max_length = 64 )
    value   = models.CharField( max_length = 64 )


class Input_Device_Callback_Action( SvenAbstract ):
    input_device    = models.ForeignKey( Device, related_name='input_device' )
    output_device   = models.ForeignKey( Device, related_name = 'output_device' )
    action          = models.CharField( max_length = 128 )
    parameters      = models.TextField( null = True, blank = True ) # This is a json_encoded list of key->value pairs that will be passed to the daemon
    conditions      = models.TextField( null = True, blank = True ) # This is a json_encoded list of key->value pairs that will be passed to the daemon
    order           = models.IntegerField( default = 0 )
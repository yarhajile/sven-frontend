from django.db import models

class SvenAbstract( models.Model ):
    created = models.DateTimeField( auto_now_add = True )
    updated = models.DateTimeField( auto_now = True, auto_now_add = True )

    class Meta:
        abstract = True


class SvenAbstractNDA( SvenAbstract ):

    """
    Create Name, Description and Active fields
    """
    name            = models.CharField( max_length = 255, null = True, blank = True )
    description     = models.TextField( null = True, blank = True )
    active          = models.BooleanField( default = True )

    class Meta:
        abstract = True


    def __str__( self ):
        return self.name


class Database_Type( SvenAbstractNDA ):
    pass


class Interface_Type( SvenAbstractNDA ):
    pass


class Interface( SvenAbstractNDA ):
    type                = models.ForeignKey( Interface_Type )
    web_socket_host     = models.CharField( max_length = 128 )
    web_socket_port     = models.IntegerField( )
    daemon_db_type      = models.ForeignKey( Database_Type )
    daemon_db_host      = models.CharField( max_length = 64 )
    daemon_db_port      = models.IntegerField( )
    daemon_db_user      = models.CharField( max_length = 64 )
    daemon_db_pass      = models.CharField( max_length = 64 )

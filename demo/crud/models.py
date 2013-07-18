from django.core.urlresolvers import reverse
from django.db import models

class Widget( models.Model ):
    name = models.CharField( max_length = 10 )
    sku  = models.IntegerField()
    
    def get_absolute_url( self ):
        return reverse( 'widget', kwargs = {'pk' : self.pk } )

    def get_create_url( self ):
        return reverse( 'widget_create' )

    def get_list_url( self ):
        return reverse( 'widgets' )

    def get_delete_url( self ):
        return reverse( 'widget_delete', kwargs = {'pk' : self.pk } )

    def get_update_url( self ):
        return reverse( 'widget_update', kwargs = {'pk' : self.pk } )

    def __unicode__( self ):
        return '%s' % ( self.name )
    
    class Meta:
        verbose_name = "Widget"
        verbose_name_plural = "Widgets"

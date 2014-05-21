from django.core.urlresolvers import reverse
from django.db import models
from bsct.models import BSCTModelMixin

class Widget( BSCTModelMixin, models.Model ):
    name = models.CharField( max_length = 10 )
    sku  = models.IntegerField()

    def sku_detail( self ):
        return 'SKU_%d' % ( self.sku )

    def __unicode__( self ):
        return '%s' % ( self.name )
    
    class Meta:
        verbose_name = "Widget"
        verbose_name_plural = "Widgets"

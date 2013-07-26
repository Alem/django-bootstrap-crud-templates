from django.core.urlresolvers import reverse

class BSCTModelMixin( object ):

    def __init__( self, *args, **kwargs ):
        super( BSCTModelMixin, self ).__init__( *args, **kwargs )
        self._bsct_name = self.__class__.__name__.lower()

    def get_absolute_url( self ):
        return reverse('%s_detail' % self._bsct_name, kwargs={'pk': self.pk } ) 

    def get_create_url( self ):
        return reverse('%s_create' % self._bsct_name )

    def get_delete_url( self ):
        return reverse('%s_delete' % self._bsct_name, kwargs={'pk': self.pk } ) 

    def get_list_url( self ):
        return reverse('%s_list' % self._bsct_name )

    def get_update_url( self ):
        return reverse('%s_update' % self._bsct_name, kwargs={'pk': self.pk } )

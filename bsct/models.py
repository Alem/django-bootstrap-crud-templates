from django.core.urlresolvers import reverse

class BSCTModelMixin( object ):
    """
    Provides a default implementation for the url defining methods.
    
    URL names are assumed to follow the format <lowercasemodelname>_<action>.
    """

    def __init__( self, *args, **kwargs ):
        """
        Set the prefix for the URL names.
        """
        super( BSCTModelMixin, self ).__init__( *args, **kwargs )

        self.bsct_view_prefix = self.__class__.__name__.lower()

    def get_absolute_url( self ):
        """
        Returns the URL of the detail page for that instance.
        """
        return reverse(
            '%s_detail' % self.bsct_view_prefix, kwargs={'pk': self.pk } 
        ) 

    def get_delete_url( self ):
        """
        Returns the URL of the deletion page for that instance.
        """
        return reverse(
            '%s_delete' % self.bsct_view_prefix, kwargs={'pk': self.pk } 
        ) 

    def get_update_url( self ):
        """
        Returns the URL of the update page for that instance.
        """
        return reverse(
            '%s_update' % self.bsct_view_prefix, kwargs={'pk': self.pk } 
        )

    def get_list_url( self ):
        """
        Returns the URL of the listing page for the model.
        """
        # This used to be a class method, however it is only called in
        # templates in the # context of a model instance, making an instance
        # method more practical. ( Avoids having to create templatetags to
        # call class method on instance class. )
        return reverse( '%s_list' % self.bsct_view_prefix )

    @classmethod
    def get_create_url( cls ):
        """
        Returns the URL of the creation page for the model.
        """
        return reverse( '%s_create' % cls.__name__.lower() )

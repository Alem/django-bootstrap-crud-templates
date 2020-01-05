from django.urls import re_path,reverse_lazy

from bsct import views as bsct_views
from django.forms import modelform_factory

class URLGenerator( object ):
    """
    Constructs and returns CRUD urls for generic BSCT views for a given model.

    URL names follow the pattern: <lower case model name>_<action>
        - ``lowercasemodelname_detail``: For the DetailView.
        - ``lowercasemodelname_create``: For the CreateView.
        - ``lowercasemodelname_list``:   For the ListView.
        - ``lowercasemodelname_update``: For the UpdateView.
        - ``lowercasemodelname_delete``: For the DeleteView.
    """

    def __init__( self, model, form_class = None, bsct_view_prefix = None ):
        """
        Internalize the model and set the view prefix. 
        """
        self.model = model
        self.bsct_view_prefix = bsct_view_prefix or model.__name__.lower()
        self.set_form_class( form_class )

    def set_form_class( self, form_class = None ):
        """
        Sets the form class to be used by the create and update views.
        """
        if form_class:
            self.form_class = form_class
        else:
            fields = self.model.get_allowed_fields()

            self.form_class = modelform_factory( 
                    self.model, 
                    fields = fields
            )

    def get_create_url( self, form_class = None, **kwargs ):
        """
        Generate the create URL for the model.
        """
        form_class = form_class if form_class else self.form_class

        return re_path( 
            r'%s/create/?$' % self.bsct_view_prefix, 
            bsct_views.CreateView.as_view( 
                model      = self.model, 
                form_class = form_class,
                **kwargs 
            ),
            name = '%s_create' % self.bsct_view_prefix,
        )

    def get_update_url( self, form_class = None, **kwargs  ):
        """
        Generate the update URL for the model.
        """
        form_class = form_class if form_class else self.form_class

        return re_path( 
            r'%s/update/(?P<pk>\d+)/?$' % self.bsct_view_prefix,
            bsct_views.UpdateView.as_view( 
                model      = self.model, 
                form_class = form_class,
                **kwargs 
            ),
            name = '%s_update' % self.bsct_view_prefix,
        )

    def get_list_url( self, **kwargs ):
        """
        Generate the list URL for the model.
        """
        return re_path(
            r'%s/(list/?)?$' % self.bsct_view_prefix,
            bsct_views.ListView.as_view( 
                model = self.model, **kwargs 
            ),
            name = '%s_list' % self.bsct_view_prefix,
        )

    def get_delete_url( self, **kwargs ):
        """
        Generate the delete URL for the model.
        """
        return re_path( 
            r'%s/delete/(?P<pk>\d+)/?$' % self.bsct_view_prefix,
            bsct_views.DeleteView.as_view( 
               model = self.model,
                success_url = reverse_lazy('%s_list' % self.bsct_view_prefix),
                **kwargs
            ), 
            name = '%s_delete' % self.bsct_view_prefix,
        )

    def get_detail_url( self, **kwargs ):
        """
        Generate the detail URL for the model.
        """
        return re_path( 
            r'%s/(?P<pk>\d+)/?$' % self.bsct_view_prefix,
            bsct_views.DetailView.as_view( 
                model = self.model, **kwargs 
                ),
            name = '%s_detail' % self.bsct_view_prefix,
        )

    def get_urlpatterns( self, crud_types = 'crudl', paginate_by = 10 ):
        """
        Generate the entire set URL for the model and return as a patterns
        object.
        Specific CRUD types may be in the string argument crud_types specified, where:
            'c' - Refers to the Create CRUD type
            'r' - Refers to the Read/Detail CRUD type
            'u' - Refers to the Update/Edit CRUD type
            'd' - Refers to the Delete CRUD type
            'l' - Refers to the List CRUD type
        """
        urlpatterns = []
        if 'c' in crud_types:
            urlpatterns.append( self.get_create_url() )
        if 'r' in crud_types:
            urlpatterns.append( self.get_detail_url() )
        if 'u' in crud_types:
            urlpatterns.append( self.get_update_url() )
        if 'l' in crud_types:
            urlpatterns.append( self.get_list_url( paginate_by = paginate_by ) )
        if 'd' in crud_types:
            urlpatterns.append( self.get_delete_url() )

        return urlpatterns

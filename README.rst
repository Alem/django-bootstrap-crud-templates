===============================
Django Bootstrap CRUD Templates
===============================

Django freed developers from the labor of writing boilerplate view logic with
class-based view; Bootstrap, the labor of designing aesthetic CSS+HTML
components.

Django Bootstrap CRUD Templates aims to unite the two, allowing developers to
simply write simple class-based views then select, or extend, a Bootstrap
template for complete CRUD exposure of a model. 

Developers can even do as little as define a model including a single mixin and
run a function to generate a set of working CRUD URLs for that model (see
Automatic Generation of Views and URLs).

Demo_

.. _Demo: http://bsct-demo.cidola.com/widget/list

Installation
-------------
1. ``pip install django-bootstrap-crud-templates``
2. Add ``'bsct'`` in the ``INSTALLED_APPS`` list in your project's settings module.

Usage
-----

Django Bootstrap CRUD Templates provides a repository of Bootstrap-integrated
Django templates.

These templates are designed to work directly with the context variables
provided by the Django Class-Based View and the attributes provided by the
Django model.

Model Requirements
~~~~~~~~~~~~~~~~~~

In order to make the most use of the features, the Model should have a few
attributes defined:

- Instance methods:
    - ``get_absolute_url``:    Returns the url to view the instance. 
      ( Minimum requirement )

    - ``get_delete_url``:      Returns the url to delete the instance.
    - ``get_update_url``:      Returns the url to update the instance.
    - ``get_list_url``:        Returns the url to list all instances.

- Class methods:
    - ``get_create_url``:      Returns the url to create an instance.
    - ``get_allowed_fields``:  Returns the list of editable fields.


For example, with a delete url named 'widget_delete', get_delete_url may be
defined as: ::
    
    def get_delete_url( self ):
        return reverse( 'widget_delete', kwargs = {'pk' : self.pk } )

You should define the model fields exposed to CRUD by defining
get_allowed_fields. ::

You can skip defining these methods by adding the ``BSCTModelMixin`` mixin
class to your model and simply naming the corresponding URLs in the following
way:

- ``lowercasemodelname_detail``: For the DetailView.
- ``lowercasemodelname_create``: For the CreateView.
- ``lowercasemodelname_update``: For the UpdateView.
- ``lowercasemodelname_delete``: For the DeleteView.
- ``lowercasemodelname_list``:   For the ListView.

Note: It is still recommended to define get_allowed_fields in your model,
otherwise it will fallback to the dangerous default of exposing ALL model
fields.

Customizing display of model fields
###################################
The default detail views simply print the value of each field.

If you desire something more than the printed value for any field, simply
define a detail method ('<field>_detail') for that field::

    class Widget( models.Model )

        sku = models.IntegerField()

        def sku_detail( self ):
            return 'SKU_%d' % ( self.sku )

View Requirements
~~~~~~~~~~~~~~~~~
To use a template directly, as opposed to extending it, simply assign its name
to the `template_name` attribute of the class-based view. ::

    # in views.py
    class CreateWidget( generic.CreateView ):
        model = models.Widget
        template_name = 'bsct/plain/form.html'

Template Requirements
~~~~~~~~~~~~~~~~~~~~~
By default, the template extends from 'base.html' and populates the 
block BSCT_MAIN. 
Therefore, you will need to have a template named 'base.html'
and it must contain the block BSCT_MAIN ::
    
    # base.html
    {% block BSCT_MAIN %}
    {% endblock %}

If you want to use the CDN-delivered version of Bootstrap included in the
package make sure your base template also defined the block BSCT_CSS ::

    # base.html
    {% block BSCT_CSS %}
    {% endblock %}

    </head>
    <body>

    {% block BSCT_MAIN %}
    {% endblock %}

If you wish to have the template extend from a template other than 'base.html',
simply provide its name as the value for the context variable 'bsct_base'. ::

    #in views.py
    class CreateWidget( generic.CreateView ):
        model = models.Widget,
        template_name = 'bsct/plain/form.html'
        
        def get_context_data(self, **kwargs):
            context = super(CreateWidget, self).get_context_data(**kwargs)

            context[ 'bsct_base' ] = 'my_special_widget_base.html'
            return context

Automatic Generation of Views and URLs
--------------------------------------

You can skip the manual definition of both views and their URLs by using
bsct.urls.URLGenerator to generate a set of URLs (and views) and including them in your applications urlpatterns::

    from bsct.urls import URLGenerator
    from crud import models

    bsct_patterns = URLGenerator( models.Widget ).get_urlpatterns()

    urlpatterns = [
        url( '', include( bsct_patterns ) )
    ]

You may also choose to have only a select few URLs automatically generated::

    
    bsct_patterns = URLGenerator( models.Widget ).get_urlpatterns( crud_types = 'rud')

    #'c' - Refers to the Create CRUD type
    #'r' - Refers to the Read/Detail CRUD type
    #'u' - Refers to the Update/Edit CRUD type
    #'d' - Refers to the Delete CRUD type
    #'l' - Refers to the List CRUD type


Template Customization
----------------------
Customizing these templates is as simple as creating your own template and
including the desired Django Bootstrap CRUD Templates template. ::

    # widget_list.html
    {% extends 'bsct/plain/list.html' %}

    {% block BSCT_LIST_ACTIONS %}
        <a href='{% object.use_widget %}'> Use Widget </a>   
    {% endblock %}

The default 'bsct/base.html' links to a CDN-hosted minified Bootstrap
CSS file. If you prefer to use your own version, simply override the block
BSCT_BOOTSTRAP_CDN. ::

    {% block BSCT_BOOTSTRAP_CDN %}
    {% endblock %}

Built for developers, by developers
-----------------------------------
Django Bootstrap CRUD Templates is an open source project that ultimately aims to
host a collection of user-submitted Bootstrap template-sets for Django. 

If you have a set of Bootstrap templates you wish to include, simply 
follow the five steps below (assuming you have a GitHub account):

1. Fork and clone https://github.com/Alem/django-bootstrap-crud-templates.
2. Ensure your set has at least two of the following templates:

   - form.html
   - list.html
   - detail.html
   - confirm_delete.html 

3. (optional) Create a README.rst with a brief description of the template set and any other pertinent information ( external dependencies, author, homepage ).

4. Place all the files in "bsct/templates/yourthemename/".

5. Pull.

All contributed templates inherit the license of the encompassing project.

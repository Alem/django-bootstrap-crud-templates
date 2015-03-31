from django.core import serializers
from django.template import Library

register = Library()

# -------------------------
# Template Tags
# -------------------------

# CDN Resources
# -------------------------

def netdna_css( path ):
    """
    Returns a link to the named NetDNA-hosted CSS resource.
    """
    return '<link href="//netdna.bootstrapcdn.com/%s" rel="stylesheet">' % path

def netdna_js( path ):
    """
    Returns a script element sourcing the named NetDNA-hosted JavaScript
    resource.
    """
    return '<script src="//netdna.bootstrapcdn.com/%s"></script>' % path

@register.simple_tag
def bootstrap_js_cdn(version = '3.1.1'):
    """
    Returns a link to a CDN-hosted Bootstrap minified JS file.
    """
    return netdna_js("bootstrap/%s/js/bootstrap.min.js" % version )

@register.simple_tag
def bootstrap_cdn( version = '3.1.1'):
    """
    Returns a link to a CDN-hosted Bootstrap minified CSS file.
    """
    return netdna_css(
        'bootstrap/%s/css/bootstrap.min.css' % version 
    )

@register.simple_tag
def bootswatch_cdn( theme, version = '3.1.1' ):
    """
    Returns a link to the named CDN-hosted Bootstrap Swatch theme.
    """
    return netdna_css( 
        "bootswatch/%s/%s/bootstrap.min.css" % (version,theme.lower()) 
    )


# Verbose name retrievers 
# -------------------------

@register.simple_tag
def get_verbose_name( instance ):
    """
    Returns the verbose name for a model.
    """
    return instance._meta.verbose_name

@register.simple_tag
def get_verbose_name_plural( instance ):
    """
    Returns the verbose pluralized name for a model.
    """
    return instance._meta.verbose_name_plural

# Pagination Helpers
# -------------------------

@register.simple_tag
def append_querystring( request, exclude = None ):
    """
    Returns the query string for the current request, minus the GET parameters
    included in the `exclude`.
    """
    exclude = exclude or ['page']

    if request and request.GET:
        amp = '&amp;'
        return amp + amp.join(
            [ '%s=%s' % (k,v) 
                for k,v in request.GET.items()
                    if k not in exclude ]
        )

    return ''
    

# Filters
# -------------------------

@register.filter
def get_detail( instance ):
    """
    Returns a dictionary of the models fields and values.

    If the method '<field>_detail' is defined, its value is used as the
    displayed value for the field. 
    """
    details = serializers.serialize( "python", [instance] )[0]['fields']

    for field in details.keys():
        detail_method = getattr( instance, '%s_detail' % field, None )

        if detail_method:
            details[ field ] = detail_method()

    return details

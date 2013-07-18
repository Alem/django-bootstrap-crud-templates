from django.forms.models import model_to_dict as django_m2d
from django.template import Library

register = Library()

# -------------------------
# Template Tags
# -------------------------

# CDN Resources
# -------------------------

@register.simple_tag()
def netdna_cdn( path ):
    """
    Returns a link to the named NetDNA-hosted CSS resource.
    """
    return '<link href="//netdna.bootstrapcdn.com/%s" rel="stylesheet">' % path

@register.simple_tag()
def bootstrap_cdn():
    """
    Returns a link to a CDN-hosted Bootstrap minified CSS file.
    """
    return netdna_cdn('twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css')

@register.simple_tag()
def bootswatch_cdn( theme ):
    """
    Returns a link to the named CDN-hosted Bootstrap Swatch theme.
    """
    if theme.lower() in [
            "amelia","cerulean","cosmo","cyborg","flatly",
            "journal","readable","simplex","slate","spacelab",
            "spruce","superhero","united"
    ]:
        return netdna_cdn( "bootswatch/2.3.2/%s/bootstrap.min.css" % theme )
    raise Exception( "Unrecognized bootswatch theme: '%s'." % theme )


# Meta-data Extractors 
# -------------------------

@register.simple_tag()
def get_verbose_name( object ):
    """
    Returns the verbose name for a model.
    """
    return object._meta.verbose_name

@register.simple_tag()
def get_verbose_name_plural( object ):
    """
    Returns the verbose pluralized name for a model.
    """
    return object._meta.verbose_name_plural

# -------------------------
# Filters
# -------------------------

@register.filter
def model_to_dict( object ):
    """
    Converts a model into a dictionary of its fields and values.
    """
    return django_m2d( object )

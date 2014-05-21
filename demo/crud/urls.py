from django.conf.urls import patterns, include, url
from bsct.urls import URLGenerator
from crud import models

bsct_patterns = URLGenerator( models.Widget ).get_urlpatterns( paginate_by = 3 )

urlpatterns = patterns( '',
        url( '', include( bsct_patterns ) ) 
)

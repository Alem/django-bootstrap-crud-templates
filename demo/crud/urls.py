from django.urls import include,path
from bsct.urls import URLGenerator
from crud import models

bsct_patterns = URLGenerator( models.Widget ).get_urlpatterns( paginate_by = 3 )

urlpatterns = [
        path( '', include( bsct_patterns ) ) 
]


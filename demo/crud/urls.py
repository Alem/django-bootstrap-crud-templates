from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from crud import models
from bsct import views

urlpatterns = patterns('',
    url( r'widget/add/$', views.CreateView.as_view( model=models.Widget ),
        name = 'widget_create'),

    url( r'widget/update/(?P<pk>\d+)$', views.UpdateView.as_view( model=models.Widget ),
        name = 'widget_update'),

    url( r'widget/list$', views.ListView.as_view( model=models.Widget, paginate_by = 3 ), 
        name = 'widget_list'),

    url( r'widget/(?P<pk>\d+)$', views.DetailView.as_view( model=models.Widget ),
        name = 'widget_detail'),

    url( r'widget/delete/(?P<pk>\d+)$', views.DeleteView.as_view( 
            model=models.Widget,
            success_url = reverse_lazy('widgets')),
        name = 'widget_delete'
    ),
)

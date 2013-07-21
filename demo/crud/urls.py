from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from crud import models

urlpatterns = patterns('',
    url(
        r'widget/add/$', generic.CreateView.as_view( 
            model=models.Widget,
            template_name = 'bsct/plain/form.html',
        ),
        name = 'widget_create'
    ),

    url(
        r'widget/update/(?P<pk>\d+)$', generic.UpdateView.as_view( 
            model=models.Widget,
            template_name = 'bsct/plain/form.html',
        ),
        name = 'widget_update'
    ),

    url(
        r'widget/list$', generic.ListView.as_view( 
            model=models.Widget,
            template_name = 'bsct/plain/list.html',
            paginate_by = 3
        ), 
        name = 'widgets'
    ),

    url(
        r'widget/(?P<pk>\d+)$', generic.DetailView.as_view(
            model=models.Widget,
            template_name = 'bsct/plain/detail.html',
        ),
        name = 'widget'
    ),

    url(
        r'widget/delete/(?P<pk>\d+)$', generic.DeleteView.as_view( 
            model=models.Widget,
            template_name = 'bsct/plain/confirm_delete.html',
            success_url = reverse_lazy('widgets')
        ),
        name = 'widget_delete'
    ),
)

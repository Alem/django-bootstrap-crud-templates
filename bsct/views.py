"""
These views do nothing other than provide members of the 'plain' BSCT template
set as default template names.
"""
from django.views import generic

class CreateView( generic.CreateView ):
    template_name = 'bsct/plain/form.html'

class UpdateView( generic.UpdateView ):
    template_name = 'bsct/plain/form.html'

class ListView( generic.ListView ):
    template_name = 'bsct/plain/list.html'

class DetailView( generic.DetailView ):
    template_name = 'bsct/plain/detail.html'

class DeleteView( generic.DeleteView ):
    template_name = 'bsct/plain/confirm_delete.html'

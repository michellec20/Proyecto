from tokenize import group
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages


class GroupRequiredMixin(View):
    group_required = None
    url_redirect = None 

    def get_url_redirects(self):
        if self.url_redirect is None:
            return reverse_lazy('home')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        user_groups = []
        for group in request.user.groups.values_list('name', flat=True):
            user_groups.append(group)
        if len(set(user_groups).intersection(self.group_required)) <= 0:
            messages.error(self.request, 'Ocurrió un error, su usuario no tiene los permisos para ver esta página')
            return HttpResponseRedirect(self.get_url_redirects())
        return super().dispatch(request,*args,**kwargs)

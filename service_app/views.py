from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as g
from service_app import models as m

# Create your views here.

class IndexListView(g.ListView):
    model = m.Mailing
    template_name = 'service_app/index_list.html'
    context_object_name = 'context'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


class ClientsListVew(g.ListView):
    model = m.Clients
    template_name = 'service_app/clients/clients_list.html'
    context_object_name = 'context'


class ClientCreateView(g.CreateView):
    model = m.Clients
    template_name = 'service_app/clients/clients_create.html'
    fields = ('__all__')
    success_url = reverse_lazy('service_app:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["editing"] = False
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
        return super().form_valid(form)


class MailingCreateView(g.CreateView):
    model = m.Mailing
    template_name = "service_app/mailing/mailing_create.html"
    fields = ("__all__")
    success_url = reverse_lazy("service_app:index")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["clients"] = m.Clients.objects.all()
        context["editing"] = False
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
        return super().form_valid(form)


class MailingUpdateView(g.UpdateView):
    model = m.Mailing
    template_name = "service_app/mailing/mailing_create.html"
    fields = ("__all__")
    success_url = reverse_lazy("service_app:index")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["clients"] = m.Clients.objects.all()
        context["editing"] = True
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
        return super().form_valid(form)


class MailingView(g.DetailView):
    model = m.Mailing
    template_name = "service_app/mailing/mailing_view.html"
    context_object_name = 'context'


class MailingDeliteView(g.DeleteView):
    model = m.Mailing
    template_name = "service_app/mailing/mailing_delete.html"
    context_object_name = 'context'
    success_url = reverse_lazy('service_app:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs['pk'])
        return queryset
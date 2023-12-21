import random
from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic as g

from service_app import models as m
from blog_app import models as blog_models
from service_app import forms as f

from random import sample

# Create your views here.

class IndexListView(g.ListView):
    model = m.Mailing
    template_name = 'service_app/index_list.html'
    context_object_name = 'context'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailings_count'] = len(m.Mailing.objects.all())
        context['active_mailings_count'] = len(m.Mailing.objects.filter(mailing_status='ACT'))
        context['unique_clients'] = len(m.Clients.objects.all())
        context['random_post'] = self.get_random_records()
        return context
    
    @staticmethod
    def get_random_records():
        # Получаем общее количество записей в модели
        total_records = blog_models.Blog.objects.count()
        
        # Если в модели менее трех записей, выбираем все записи
        if total_records <= 3:
            random_records = blog_models.Blog.objects.all()
        else:
            # Генерируем случайные индексы записей
            random_indexes = random.sample(range(total_records), 3)
            
            # Выбираем три записи с соответствующими индексами
            random_records = blog_models.Blog.objects.filter(pk__in=random_indexes)
        
        return random_records


class ClientsListVew(g.ListView):
    model = m.Clients
    template_name = 'service_app/clients/clients_list.html'
    context_object_name = 'context'


class ClientView(g.DetailView):
    model = m.Clients
    template_name = 'service_app/clients/clients_view.html'
    context_object_name = 'context'


class ClientCreateView(g.CreateView):
    model = m.Clients
    template_name = 'service_app/clients/clients_create.html'
    success_url = reverse_lazy('service_app:index')
    form_class = f.ClientsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["editing"] = False
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
        return super().form_valid(form)


class ClientUpdateView(g.UpdateView):
    model = m.Clients
    template_name = 'service_app/clients/clients_create.html'
    form_class = f.ClientsForm
    success_url = reverse_lazy('service_app:index')
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["editing"] = True
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
        return super().form_valid(form)


class ClientDeleteView(g.DeleteView):
    model = m.Clients
    template_name = "service_app/clients/clients_delete.html"
    context_object_name = 'context'
    success_url = reverse_lazy('service_app:clients_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs['pk'])
        return queryset


class MailingCreateView(g.CreateView):
    model = m.Mailing
    template_name = "service_app/mailing/mailing_create.html"
    success_url = reverse_lazy("service_app:index")
    form_class = f.MailerForm
    context_object_name = 'context'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["editing"] = False
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
        return super().form_valid(form)


class MailingUpdateView(g.UpdateView):
    model = m.Mailing
    template_name = "service_app/mailing/mailing_create.html"
    success_url = reverse_lazy("service_app:index")
    form_class = f.MailerForm
    context_object_name = 'context'

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


def change_mailing_status(request, pk):
    mailing = get_object_or_404(m.Mailing, pk=pk)
    if mailing.mailing_status == 'ACT':
        mailing.mailing_status = 'CNL'
    else:
        mailing.mailing_status = 'ACT'
    mailing.save()
    return redirect(reverse('service_app:index'))


class LogsListView(g.ListView):
    model = m.Logs
    template_name = 'service_app/logs_list.html'
    context_object_name = 'logs'
    paginate_by = 10

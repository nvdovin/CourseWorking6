import random
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic as g

from service_app import models as m
from blog_app import models as blog_models
from service_app import forms as f
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

class IndexListView(g.ListView):
    model = m.Mailing
    template_name = 'service_app/index_list.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailings_count'] = len(m.Mailing.objects.filter(mailing_author=self.request.user))
        context['active_mailings_count'] = len(
            m.Mailing.objects.filter(mailing_status='ACT').filter(mailing_author=self.request.user))
        context['unique_clients'] = len(m.Clients.objects.filter(client_author=self.request.user))
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

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff or user.is_superuser:
                pass
            else:
                queryset = queryset.filter(mailing_author=self.request.user)
        return queryset


class ClientsListVew(g.ListView):
    model = m.Clients
    template_name = 'service_app/clients/clients_list.html'
    context_object_name = 'context'

    def get_queryset(self):
        queryset = super().get_queryset()
        new_query = queryset.filter(client_author=self.request.user)
        return new_query


class ClientView(g.DetailView):
    model = m.Clients
    template_name = 'service_app/clients/clients_view.html'
    context_object_name = 'context'


class ClientCreateView(LoginRequiredMixin, g.CreateView):
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
            w = form.save(commit=False)
            w.client_author = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, g.UpdateView):
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


class ClientDeleteView(LoginRequiredMixin, g.DeleteView):
    model = m.Clients
    template_name = "service_app/clients/clients_delete.html"
    context_object_name = 'context'
    success_url = reverse_lazy('service_app:clients_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs['pk'])
        return queryset


class MailingCreateView(LoginRequiredMixin, g.CreateView):
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
            w = form.save(commit=False)
            w.mailing_author = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Добавление дополнительных аргументов для формы
        kwargs['user'] = self.request.user.email
        return kwargs


class MailingUpdateView(LoginRequiredMixin, g.UpdateView):
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Передача пользователя в `kwargs`
        return kwargs


class MailingView(g.DetailView):
    model = m.Mailing
    template_name = "service_app/mailing/mailing_view.html"
    context_object_name = 'context'


class MailingDeliteView(LoginRequiredMixin, g.DeleteView):
    model = m.Mailing
    template_name = "service_app/mailing/mailing_delete.html"
    context_object_name = 'context'
    success_url = reverse_lazy('service_app:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs['pk'])
        return queryset


# @permission_required('service_app.change_blog')
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

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(log_author=user.email)
        return queryset

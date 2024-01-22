from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import views as v
from django.contrib.auth import forms as f
from django.urls import reverse_lazy

from config import settings
from user_app.models import User
from .forms import UserConfirmForm, UserEditForm, UserLoginForm
from django.views import generic as g
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm

import os
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required


current_email = None

# Create your views here.

class UserLoginView(v.LoginView):
    form_class = UserLoginForm
    template_name = 'user_app/user_auth.html'


class RegisterUserView(g.FormView):
    form_class = UserRegistrationForm
    template_name = 'user_app/user_register.html'
    success_url = reverse_lazy('user_app:confirm_user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = False
        return context
    

    def form_valid(self, form):
        global current_email

        secret_code = get_random_string(length=6)
        user = form.save()
        user.is_active = False
        user.set_password(form.cleaned_data['password1'])
        user.temporary_password = secret_code
        user.birthday = form.cleaned_data['birthday']
        user.phone_number = form.cleaned_data['phone_number']
        user.country = form.cleaned_data['country']
        current_email = user.email

        my_user = form.save()
        send_mail(
            subject='Подтверждение почты',
            message=f'Для продолжения регистрации введите этот код в окне регистрации\n{secret_code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[f'{my_user.email}',]
        )

        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, g.UpdateView):
    model = get_user_model()
    form_class = UserEditForm
    template_name = 'user_app/user_register.html'
    success_url = reverse_lazy('user_app:profile_view')
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = True
        return context

    def get_object(self, queryset=None):
        return self.request.user


class ProfileView(LoginRequiredMixin, g.TemplateView):
    model = get_user_model()
    template_name = 'user_app/user_view.html'
    context_object_name = 'context'
    
    def get_object(self, queryset=None):
        return self.request.user


def reset_password(request):
    new_password = get_random_string(length=10)
    email = request.user.email
    send_mail(
            subject='Новый пароль',
            message=f'Новый пароль для пользователя {email}\n"{new_password}"',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[f'{email}',]
        )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse_lazy('user_app:login_user'))


class ConfirmEmailView(g.FormView):
    template_name = 'user_app/user_confirm.html'
    form_class = UserConfirmForm
    success_url = reverse_lazy('user_app:login_user')
    global current_email

    def form_valid(self, form):
        temp_password_f = form.cleaned_data['temporary_password']
        user = User.objects.get(email=current_email)

        temp_password_u = user.temporary_password
        print(temp_password_f, temp_password_u)

        if temp_password_u == temp_password_f:
            user.is_active = True
            user.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)


def delete_avatar(request):
    request.user.avatar = None
    request.user.save()
    return redirect(reverse_lazy('user_app:update_user'))


@permission_required('user_app.change_user')
def change_profile_status(request, pk):
    users = get_object_or_404(User, pk=pk)
    if users.is_active == True:
        users.is_active = False
    else:
        users.is_active = True
    users.save()
    return redirect(reverse_lazy('user_app:users_list'))


class UsersListView(LoginRequiredMixin, g.ListView):
    model = User
    template_name = 'user_app/user_list_view.html'
    context_object_name = 'context'


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import DetailView, View
from user_app import views as v

app_name = 'user_app'

urlpatterns = [
    path('login_user/', v.UserLoginView.as_view(), name='login_user'),
    path('logout_user/', LogoutView.as_view(), name='logout_user'),
    path('register_user/', v.RegisterUserView.as_view(), name='register_user'),
    path('confirm_user/', v.ConfirmEmailView.as_view(), name='confirm_user'),
    path('reset_password/', v.reset_password, name='reset_password'),
    path('delete_avatar/', v.delete_avatar, name='delete_avatar'),
    path('update_user/', v.UpdateProfileView.as_view(), name='update_user'),
    path('profile_view/', v.ProfileView.as_view(), name='profile_view'),

]
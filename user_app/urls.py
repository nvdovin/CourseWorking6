from django.urls import path
from django.contrib.auth.views import LogoutView
from user_app import views as v
from django.views.decorators.cache import cache_page

app_name = 'user_app'

urlpatterns = [
    path('login_user/', cache_page(16*60)(v.UserLoginView.as_view()), name='login_user'),
    path('logout_user/', cache_page(16*60)(LogoutView.as_view()), name='logout_user'),
    path('register_user/', v.RegisterUserView.as_view(), name='register_user'),
    path('confirm_user/', v.ConfirmEmailView.as_view(), name='confirm_user'),
    path('reset_password/', v.reset_password, name='reset_password'),
    path('delete_avatar/', cache_page(16*60)(v.delete_avatar), name='delete_avatar'),
    path('update_user/', v.UpdateProfileView.as_view(), name='update_user'),
    path('profile_view/', cache_page(16*60)(v.ProfileView.as_view()), name='profile_view'),
    path('users_list/', v.UsersListView.as_view(), name='users_list'),
    path('change_profile_status_<int:pk>/', cache_page(16*60)(v.change_profile_status), name='change_profile_status'),

]
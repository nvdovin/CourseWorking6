"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

from django.urls import path
from service_app import views as v
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', v.IndexListView.as_view(), name='index'),
    path('clients_list/', v.ClientsListVew.as_view(), name='clients_list'),
    path('view_client_<int:pk>/', v.ClientView.as_view(), name='view_client'),
    path('create_client/', v.ClientCreateView.as_view(), name='create_client'),
    path('update_client_<int:pk>/', v.ClientUpdateView.as_view(), name='update_client'),
    path('delete_client_<int:pk>/', v.ClientDeleteView.as_view(), name='delete_client'),
    path('create_mailer/', v.MailingCreateView.as_view(), name='create_mailer'),
    path('edit_mailer_<int:pk>/', v.MailingUpdateView.as_view(), name='edit_mailer'),
    path('view_mailer_<int:pk>/', v.MailingView.as_view(), name='view_mailer'),
    path('delete_mailer_<int:pk>/', v.MailingDeliteView.as_view(), name='delete_mailer'),
    path('change_status_mailer_<int:pk>/', v.change_mailing_status, name='status_mailer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
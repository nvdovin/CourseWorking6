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
    path('create_client/', v.ClientCreateView.as_view(), name='create_client'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
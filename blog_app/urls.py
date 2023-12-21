from django.urls import path
from blog_app.apps import BlogAppConfig
from blog_app import views as v

app_name = BlogAppConfig.name


urlpatterns = [
    path('all_posts/', v.PostsListView.as_view() , name='all_posts'),
    path('create/', v.PostCreateView.as_view(), name='create'),
    path('<int:pk>/view/', v.PostDetailView.as_view() , name='view'),
    path('<int:pk>/edit/', v.PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', v.PostDeleteView.as_view() , name='delete'),

    path('login/', v.LogInView.as_view() , name='login'),
    path('logout/', v.LogOutView.as_view() , name='logout'),


]
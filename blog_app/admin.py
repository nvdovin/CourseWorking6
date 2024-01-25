from django.contrib import admin
from blog_app.models import Blog
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    search_fields = ('title', 'content', 'is_published')
    list_filter = ['is_published']
from django.contrib import admin
from service_app import models as m

# Register your models here.

@admin.register(m.Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)
    search_fields = ('email', 'name')
from django.contrib import admin
from service_app import models as m

# Register your models here.


@admin.register(m.Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)
    search_fields = ('email', 'name')


@admin.register(m.Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('mail_header', 'mailing_status')
    list_filter = ('mail_header',)
    search_fields = ('mail_header', 'mail_message')
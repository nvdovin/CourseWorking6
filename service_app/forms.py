from collections.abc import Mapping
from typing import Any
from django.forms.utils import ErrorList
from service_app import models as m
from django import forms


class MailerForm(forms.Form):
    mailing_time = forms.TimeField(label='Время рассылки', )
    mailing_period = forms.ChoiceField(label='Период рассылки', required=False, choices=(
        (None, 'Весь день'),
        ('PD', 'Раз в сутки'), 
        ('PW', 'Раз в неделю'), 
        ('PM', 'Раз в месяц')
    ))
    mailing_status = forms.ChoiceField(label='Статус рассылки', initial=('ACT', 'Активна'), choices=(
        ('CNL', 'Не активна'),
        ('ACT', 'Активна')
    ))
    mailing_day = forms.ChoiceField(label='День рассылки', required=False, choices=(
        (None, 'Каждый день'),
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье')
    ))
    mailing_day_of_month = forms.IntegerField(max_value=31, label='День в месяце', required=False)
    mail_header = forms.CharField(label='Тема письма')
    mail_message = forms.CharField(label='Текст письма', widget=forms.Textarea)
    recepient = forms.ModelMultipleChoiceField(label='Адресант', queryset=m.Clients.objects.all())

    class Meta:
        model = m.Mailing
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
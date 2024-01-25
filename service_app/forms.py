from collections.abc import Mapping
from typing import Any
from django.forms.utils import ErrorList
from service_app import models as m
from django import forms


class MailerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['recepient'].queryset = m.Clients.objects.filter(client_author=user)
        print(m.Clients.objects.filter(client_author=user))

    mailing_time = forms.TimeField(label='Время рассылки', required=False,
                                   widget=forms.TimeInput(attrs={'class': 'same-widht'}))
    mailing_period = forms.ChoiceField(label='Период рассылки', required=False, choices=(
        (None, 'Весь день'),
        ('PD', 'Раз в сутки'),
        ('PW', 'Раз в неделю'),
        ('PM', 'Раз в месяц')), widget=forms.Select(attrs={'class': 'same-widht'}))
    mailing_status = forms.ChoiceField(label='Статус рассылки', initial=('CRT', 'Создана'), choices=(
        ('CNL', 'Завершена'),
        ('CRT', 'Создана'),
        ('ACT', 'Запущена')), widget=forms.Select(attrs={'class': 'same-widht'}))
    mailing_day = forms.ChoiceField(label='День рассылки', required=False, choices=(
        (None, 'Каждый день'),
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье')), widget=forms.Select(attrs={'class': 'same-widht'}))
    mailing_day_of_month = forms.IntegerField(max_value=31, label='День в месяце', required=False,
                                              widget=forms.TextInput(attrs={'class': 'same-widht'}))
    mail_header = forms.CharField(label='Тема письма', widget=forms.TextInput(attrs={'class': 'same-widht'}))
    mail_message = forms.CharField(label='Текст письма',
                                   widget=forms.Textarea(attrs={'class': 'same-widht same-height'}))
    recepient = forms.ModelMultipleChoiceField(label='Адресанты', queryset=m.Clients.objects.all(),
                                               widget=forms.SelectMultiple(attrs={'class': 'same-widht'}))

    class Meta:
        model = m.Mailing
        exclude = ['mailing_author']


class ClientsForm(forms.ModelForm):
    email = forms.CharField(max_length=200,
                            label='Электронная почта',
                            widget=forms.TextInput(attrs={'class': 'same-widht'}))
    name = forms.CharField(max_length=200, label='Имя', widget=forms.TextInput(attrs={'class': 'same-widht'}))
    surame = forms.CharField(max_length=200, label='Фамилия', widget=forms.TextInput(attrs={'class': 'same-widht'}))
    fathers_name = forms.CharField(max_length=200, label='Отчество', required=False,
                                   widget=forms.TextInput(attrs={'class': 'same-widht'}))
    comment = forms.Field(label='Комментарий', widget=forms.Textarea(attrs={'class': 'same-widht same-height'}))

    class Meta:
        model = m.Clients
        exclude = ['client_author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email and '.' not in email:
            raise forms.ValidationError('Это не эмейл, чувак')
        return email

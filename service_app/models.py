from django.db import models

# Create your models here.

class Clients(models.Model):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, db_index=True)
    name = models.CharField(max_length=100, verbose_name='Имя')
    surame = models.CharField(max_length=100, verbose_name='Фамилия')
    fathers_name = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    mailing_time = models.TimeField(verbose_name='Время рассылки')
    mailing_period = models.CharField(max_length=50, verbose_name='Период рассылки')
    mailing_status = models.CharField(max_length=50, verbose_name='Статус рассылки')

    mail_header = models.CharField(max_length=150, verbose_name='Тема письма')
    mail_message = models.TextField(verbose_name='Текст письма')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Logs(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Последняя попытка')
    status = models.CharField(max_length=50, verbose_name='Статус попытки')
    response = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ответ почтового сервера')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
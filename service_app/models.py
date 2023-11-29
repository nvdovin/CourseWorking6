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
    
    def __str__(self) -> str:
        return f'{self.name} {self.surame} ({self.email})'


class Mailing(models.Model):
    mailing_time = models.TimeField(verbose_name='Время рассылки')
    mailing_period = models.CharField(max_length=50, verbose_name='Период рассылки', choices=(
        ('PD', 'Раз в сутки'), 
        ('PW', 'Раз в неделю'), 
        ('PM', 'Раз в месяц')))
    mailing_status = models.CharField(max_length=50, verbose_name='Статус рассылки',choices=(
        ('CNL', 'Не активна'),
        ('ACT', 'Активна'),
    ))

    mail_header = models.CharField(max_length=150, verbose_name='Тема письма')
    mail_message = models.TextField(verbose_name='Текст письма')

    recepient = models.ManyToManyField(to=Clients, related_name='recepirnts', blank=True, null=True, verbose_name='Адресант')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'{self.mail_header}, {self.mailing_status}'


class Logs(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Последняя попытка')
    status = models.CharField(max_length=50, verbose_name='Статус попытки')
    response = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ответ почтового сервера')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
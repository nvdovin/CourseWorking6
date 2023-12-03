# Generated by Django 4.2.7 on 2023-12-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0011_alter_mailing_mailing_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='mailing_day',
            field=models.CharField(blank=True, choices=[('mon', 'Понедельник'), ('tue', 'Вторник'), ('wed', 'Среда'), ('thu', 'Четверг'), ('fri', 'Пятница'), ('sat', 'Суббота'), ('sun', 'Воскресенье')], null=True, verbose_name='День рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='mailing_period',
            field=models.CharField(blank=True, choices=[('PD', 'Раз в сутки'), ('PW', 'Раз в неделю'), ('PM', 'Раз в месяц')], max_length=50, null=True, verbose_name='Период рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='mailing_status',
            field=models.CharField(choices=[('CNL', 'Не активна'), ('ACT', 'Активна')], default=('ACT', 'Активна'), max_length=50, verbose_name='Статус рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='mailing_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время рассылки'),
        ),
    ]

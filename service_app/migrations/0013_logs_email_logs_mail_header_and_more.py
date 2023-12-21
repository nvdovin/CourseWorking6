# Generated by Django 4.2.7 on 2023-12-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0012_alter_mailing_mailing_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='email',
            field=models.CharField(default=None, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='logs',
            name='mail_header',
            field=models.CharField(default=None, null=True, verbose_name='Рассылка'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='mailing_day',
            field=models.CharField(blank=True, choices=[(None, 'Каждый день'), ('mon', 'Понедельник'), ('tue', 'Вторник'), ('wed', 'Среда'), ('thu', 'Четверг'), ('fri', 'Пятница'), ('sat', 'Суббота'), ('sun', 'Воскресенье')], null=True, verbose_name='День рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='mailing_period',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Период рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='mailing_status',
            field=models.CharField(choices=[('CNL', 'Завершена'), ('CRT', 'Создана'), ('ACT', 'Запущена')], max_length=50, verbose_name='Статус рассылки'),
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0008_alter_mailing_mailing_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='mail_header',
            field=models.CharField(max_length=150, unique=True, verbose_name='Тема письма'),
        ),
    ]

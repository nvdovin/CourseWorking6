# Generated by Django 4.2.7 on 2023-11-26 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0002_mailing_recepients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailing',
            old_name='recepients',
            new_name='recepient',
        ),
    ]

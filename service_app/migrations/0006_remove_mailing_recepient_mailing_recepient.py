# Generated by Django 4.2.7 on 2023-11-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0005_alter_mailing_mailing_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='recepient',
        ),
        migrations.AddField(
            model_name='mailing',
            name='recepient',
            field=models.ManyToManyField(blank=True, null=True, related_name='recepirnts', to='service_app.clients', verbose_name='Адресант'),
        ),
    ]

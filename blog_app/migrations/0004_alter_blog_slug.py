# Generated by Django 4.2.5 on 2023-11-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blog_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=100, verbose_name='Slug'),
        ),
    ]

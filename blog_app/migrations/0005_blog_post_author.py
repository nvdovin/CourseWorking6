# Generated by Django 4.2.7 on 2023-12-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_author',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Автор'),
        ),
    ]

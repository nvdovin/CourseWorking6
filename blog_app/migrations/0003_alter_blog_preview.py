# Generated by Django 4.2.5 on 2023-10-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_blog_content_alter_blog_views_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/media', verbose_name='Превью'),
        ),
    ]
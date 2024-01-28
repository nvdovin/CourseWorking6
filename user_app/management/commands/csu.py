from django.core.management import BaseCommand
from user_app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@rassilnik.ru',
            first_name='admin',
            last_name='rassilnik',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('admin')
        user.save()
        
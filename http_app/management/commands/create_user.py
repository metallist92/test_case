from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import re
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Input new user username:')
        new_username = input()
        if not bool(re.match('\S+', new_username)):
            raise CommandError('Имя содержит недопустимые символы')
        print('Input new user password:')
        password = input()
        try:
            user, created = User.objects.get_or_create(username=new_username, password=password, is_active=True, is_staff=False, is_superuser=False)
        except Exception as e:
            raise CommandError('Не удалось создать пользователя')
        else:
            if not created:
                raise CommandError('Пользователь уже существует')
            token = Token.objects.create(user=user)
            print(f'User {str(user)} created with token: {str(token)}')

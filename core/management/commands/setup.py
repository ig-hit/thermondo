import os
import random
import string

import django.contrib.auth.models
from django.core import management


class Command(management.BaseCommand):
    def handle(self, *args, **kwargs):
        # Setup initial admin user
        password = os.environ.get(
            "INITIAL_SUPERUSER_PASSWORD",
            self._generate_temp_password(random.randint(8, 12)),
        )
        try:
            user = django.contrib.auth.models.User.objects.get(username="jane.doe")
            user.set_password(password)
            user.save()
            print(f'User "jane.doe" updated, please change the initial password: "{password}".')
        except django.contrib.auth.models.User.DoesNotExist:
            django.contrib.auth.models.User.objects.create_superuser(
                username="jane.doe",
                password=password,
            )
            print(f'User "jane.doe" created, please change the initial password: "{password}".')

    def _generate_temp_password(self, length):
        chars = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(chars) for _ in range(length))

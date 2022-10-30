import django.contrib.auth.models

import testing.factories


class UserFactory(testing.factories.BaseFactory):
    def create(self, **kwargs):
        defaults = {
            "username": "john.doe",
            "email": "john.doe@example.com",
            "password": "password",
            "first_name": "John",
            "last_name": "Doe",
            "is_staff": False,
            "is_active": True,
        }
        merged = {**defaults, **kwargs}
        model = django.contrib.auth.models.User

        try:
            user = model.objects.get(username=merged["username"])
        except model.DoesNotExist:
            user = model(**merged)
            user.set_password(merged["password"])
            user.save()
        return user


user_factory = UserFactory()

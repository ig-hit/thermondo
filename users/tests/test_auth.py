from unittest import mock

import django.contrib.auth.models
from django import test
from rest_framework import exceptions

from users import auth

entity = django.contrib.auth.models.User


class TokenAuthTest(test.TestCase):
    @mock.patch("users.auth.django.contrib.auth.models.User.objects.get")
    def test_get_user(self, user_mock):
        user = entity(id=1212, is_active=True, username="foo")
        user_mock.return_value = user
        validated_token = {"user_id": 1212}
        res = auth.TokenAuth().get_user(validated_token)
        self.assertEqual(res, user)

    @mock.patch("users.auth.django.contrib.auth.models.User.objects.get")
    def test_get_user_not_found(self, user_mock):
        user_mock.side_effect = entity.DoesNotExist()
        validated_token = {"user_id": 1212}

        with self.assertRaises(exceptions.AuthenticationFailed) as ctx:
            auth.TokenAuth().get_user(validated_token)

        self.assertEqual(ctx.exception.get_full_details().get("code"), "auth_user_not_found")

    @mock.patch("users.auth.django.contrib.auth.models.User.objects.get")
    def test_get_user_inactive(self, user_mock):
        login_user = entity(id=1212, is_active=False)
        user_mock.return_value = login_user
        validated_token = {"user_id": 1212}

        with self.assertRaises(exceptions.AuthenticationFailed) as ctx:
            auth.TokenAuth().get_user(validated_token)

        self.assertEqual(ctx.exception.get_full_details().get("code"), "auth_user_inactive")

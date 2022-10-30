from unittest import mock

import django.contrib.auth.models
from django import test

from users import serializers


class TestTokenObtainPairSerializer(test.TestCase):
    def test_token_enhance(self):
        user = mock.MagicMock(username="foo", pk=1)
        data = {}
        res = serializers.token_enhance(data, user)
        assert res == {"username": "foo", "id": 1}

    @mock.patch("users.serializers.token_enhance")
    @mock.patch("rest_framework_simplejwt.serializers.TokenObtainPairSerializer.validate")
    @mock.patch("users.serializers.TokenObtainPairSerializer.get_token")
    def test_validate(self, get_token, parent_validator, token_enhance):
        get_token.return_value = mock.MagicMock(access_token={})
        data = {}
        user = django.contrib.auth.models.User(username="foo")
        obj = serializers.TokenObtainPairSerializer(data=data)
        obj.user = user

        _ = obj.validate(
            {
                "username": "foo",
                "password": "bar",
            }
        )
        parent_validator.assert_called_once()
        token_enhance.assert_called_once()


class TestRegistrationSerializer:
    def test_save(self):
        ...

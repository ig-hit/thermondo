import django.contrib.auth.models
import rest_framework_simplejwt.authentication
import rest_framework_simplejwt.exceptions
import rest_framework_simplejwt.settings
from rest_framework import exceptions

from users import errors


class TokenAuth(rest_framework_simplejwt.authentication.JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token[rest_framework_simplejwt.settings.api_settings.USER_ID_CLAIM]
        except KeyError:
            raise rest_framework_simplejwt.exceptions.InvalidToken(
                "Token contained no recognizable user identification"
            )

        try:
            user = django.contrib.auth.models.User.objects.get(id=user_id)
        except django.contrib.auth.models.User.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                errors.Errors.AUTH_USER_NOT_FOUND.value,
                code=errors.Errors.AUTH_USER_NOT_FOUND.name.lower(),
            )

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                errors.Errors.AUTH_USER_INACTIVE.value,
                code=errors.Errors.AUTH_USER_INACTIVE.name.lower(),
            )

        return user

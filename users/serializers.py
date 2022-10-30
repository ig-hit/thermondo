import django.contrib.auth.models
import rest_framework_simplejwt.serializers
from rest_framework import exceptions, serializers

from users import errors


def token_enhance(access, user: django.contrib.auth.models.User):
    access["username"] = user.username
    access["id"] = user.pk

    return access


class TokenObtainPairSerializer(rest_framework_simplejwt.serializers.TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        if not isinstance(user, django.contrib.auth.models.User):
            raise exceptions.PermissionDenied(detail=errors.Errors.AUTH_USER_MISMATCH.value)

        if not data:
            data = {}

        refresh = self.get_token(user)
        access = refresh.access_token

        access = token_enhance(access, user)

        data["refresh"] = str(refresh)
        data["access"] = str(access)

        return data


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = django.contrib.auth.models.User
        fields = (
            "username",
            "password",
            "password2",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = django.contrib.auth.models.User(username=self.validated_data["username"])
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": errors.Errors.PASSWORDS_MUST_MATCH})
        user.set_password(password)
        user.save()
        return user

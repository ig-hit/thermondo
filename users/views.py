from rest_framework import mixins, permissions, viewsets
from rest_framework_simplejwt import views

from users import serializers


class TokenView(views.TokenObtainPairView):
    serializer_class = serializers.TokenObtainPairSerializer


class RegistrationView(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.RegistrationSerializer

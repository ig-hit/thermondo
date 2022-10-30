from rest_framework import filters, mixins, permissions, viewsets

from notes import models, serializers
from users import auth


class NotesView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    authentication_classes = [auth.TokenAuth]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.NotesSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ["@body"]

    def get_object(self):
        return self.get_queryset().filter(id=self.kwargs.get("pk")).first()

    def get_queryset(self):
        params = {}
        user = self.request.user
        if not user.id:
            params["is_public"] = True
        else:
            params["user_id"] = user.id

        with_tags = self.request.query_params.getlist("tag")
        if with_tags:
            params["tags__name__in"] = with_tags

        return models.Note.objects.filter(**params)

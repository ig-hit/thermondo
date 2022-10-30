import taggit.serializers
from rest_framework import serializers

from notes import models


class NotesSerializer(
    taggit.serializers.TaggitSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        rel_name = "Notes"
        model = models.Note
        fields = (
            "id",
            "title",
            "body",
            "tags",
            "is_public",
        )

    tags = taggit.serializers.TagListSerializerField(default=[])

    def validate(self, attrs):
        return {
            **attrs,
            "user_id": self.context["request"].user.id,
        }

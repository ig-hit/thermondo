import testing.factories
from notes import serializers


class NotesFactory(testing.factories.BaseFactory):
    def create(self, user_id, **kwargs):
        defaults = {
            "title": "Title",
            "body": "Body",
            "user_id": user_id,
            "tags": [],
            "is_public": False,
        }
        merged = {**defaults, **kwargs}
        obj = serializers.NotesSerializer().create(merged)

        return obj


notes_factory = NotesFactory()

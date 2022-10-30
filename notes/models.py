import django.contrib.auth.models
import django.db.models
from taggit import managers

from core import models


class Note(models.TimestampableMixin):
    class Meta:
        db_table = "notes"
        verbose_name_plural = "Notes"
        ordering = ["-id"]

    title = django.db.models.CharField(max_length=256)  # type: ignore
    # todo(igor): verify max length of the body field, change field accordingly
    body = django.db.models.TextField(db_index=True)  # type: ignore
    is_public = django.db.models.BooleanField(default=False, db_index=True)  # type: ignore
    tags = managers.TaggableManager(blank=True)
    user = django.db.models.ForeignKey(
        django.contrib.auth.models.User,
        on_delete=django.db.models.CASCADE,
        related_name="user",
    )  # type: ignore

    def __str__(self):
        return self.title

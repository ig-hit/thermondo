from django.db import models


class TimestampableMixin(models.Model):
    class Meta:
        abstract = True

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True, editable=False)

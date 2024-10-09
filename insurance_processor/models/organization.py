from django.db import models


class Organization(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    organisation_id = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

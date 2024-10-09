from django.db import models


class Insurer(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )

    insurer_unique_id = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

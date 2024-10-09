from django.db import models

from insurance_processor.models import Insurer


class Plan(models.Model):
    name = models.CharField(
        max_length=255
    )

    insurer = models.ForeignKey(
        Insurer,
        on_delete=models.CASCADE,
        related_name='plan'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = (('name', 'insurer'),)

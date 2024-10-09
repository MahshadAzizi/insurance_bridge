from django.db import models


class Policy(models.Model):
    policy_start_date = models.DateField()

    policy_end_date = models.DateField()

    policy_unique_id = models.IntegerField()

    confirmation_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

from django.db import models

from insurance_processor.models import Policy, Plan, Organization
from users.models import User


class Insured(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    policy = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    insured_id = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

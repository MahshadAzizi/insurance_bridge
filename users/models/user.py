from django.db import models


class User(models.Model):
    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    mobile_number = models.CharField(
        max_length=15
    )

    national_code = models.CharField(
        max_length=10
    )

    birth_date = models.DateField()

    father_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    place_of_issue = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

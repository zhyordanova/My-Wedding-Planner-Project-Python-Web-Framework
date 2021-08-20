from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from my_wedding_planner.core.utils import phoneNumberRegex

UserModel = get_user_model()


class MyWeddingPlannerProfile(models.Model):
    first_name = models.CharField(
        max_length=30,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
    )

    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        validators=[phoneNumberRegex],
        max_length=16,
        blank=True,
        null=True,
    )

    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    is_complete = models.BooleanField(
        default=False,
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"


from .signals import *

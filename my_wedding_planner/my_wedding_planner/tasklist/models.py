from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator

UserModel = get_user_model()


class TaskList(models.Model):
    CATEGORY_CHOICE_RECEPTION = 'Reception'
    CATEGORY_CHOICE_CEREMONY = 'Ceremony'
    CATEGORY_CHOICE_TRANSPORTATION = 'Transportation'
    CATEGORY_CHOICE_DECORATION = 'Decoration'
    CATEGORY_CHOICE_PHOTO_AND_VIDEO = 'Photo and Video'
    CATEGORY_CHOICE_PHOTO_ENTERTAINMENT = 'Entertainment'
    CATEGORY_CHOICE_PHOTO_ATTIRE_AND_ACCESSORIES = 'Attire and Accessories'

    CATEGORY_CHOICES = [
        (CATEGORY_CHOICE_RECEPTION, 'Reception'),
        (CATEGORY_CHOICE_CEREMONY, 'Ceremony'),
        (CATEGORY_CHOICE_TRANSPORTATION, 'Transportation'),
        (CATEGORY_CHOICE_DECORATION, 'Decoration'),
        (CATEGORY_CHOICE_PHOTO_AND_VIDEO, 'Phone and video'),
        (CATEGORY_CHOICE_PHOTO_ENTERTAINMENT, 'Entertainment'),
        (CATEGORY_CHOICE_PHOTO_ATTIRE_AND_ACCESSORIES, 'Attire and accessories'),
    ]

    name = models.CharField(
        max_length=100,
    )

    quest_capacity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )

    budget = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ]
    )

    note = models.TextField()

    image = models.ImageField(
        upload_to='tasklist',
        blank=True,
        null=True,
    )

    url = models.URLField(
        max_length=200,
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    task = models.ForeignKey(
        TaskList,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    comment = models.TextField()

    task = models.ForeignKey(
        TaskList,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

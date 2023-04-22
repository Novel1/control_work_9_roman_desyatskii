from django.contrib.auth.models import User
from django.db import models

from webapp.models import Photo


class Favorite(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='favorite_photo',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
        to=Photo,
        related_name='favorite_users',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )




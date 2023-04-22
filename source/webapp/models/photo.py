from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class Photo(models.Model):
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='images',
        verbose_name='Аватар'
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Подпись'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    users = models.ManyToManyField(
        through='webapp.Favorite',
        to=User,
        related_name='photos'
    )



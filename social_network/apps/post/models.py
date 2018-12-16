from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255
    )

    text = models.TextField(
        verbose_name=_('Text'),
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        User,
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )

    likes = models.ManyToManyField(
        User,
        verbose_name=_('Likes'),
        related_name='liked_posts'
    )

    def __str__(self):
        return self.title

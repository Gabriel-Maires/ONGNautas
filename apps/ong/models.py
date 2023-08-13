from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class Project(models.Model):

    title = models.CharField(_('title'), max_length=24, blank=False)
    short_description = models.CharField(_('short description'), max_length=64, blank=False)
    description = models.TextField(_('description'))
    address = models.CharField(_('address'), max_length=50)
    image = models.ImageField(_('image'), upload_to='projects')
    is_active = models.BooleanField(_('is active'), default=True)
    amount_spent = models.DecimalField(_('amount spent'), max_digits=6, decimal_places=2, default=0.0)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    CATEGORY_CHOICES = [('F', 'Forest'), ('W', 'Water'), ('A', 'Air')]

    title = models.CharField(_('title'), max_length=24, blank=False)
    text = models.TextField(_('text'), blank=False)
    category = models.CharField(_('category'), max_length=1, choices=CATEGORY_CHOICES, blank=False)
    image = models.ImageField(_('image'), upload_to='blog_posts')
    date = models.DateField(_('date'), default=datetime.now())


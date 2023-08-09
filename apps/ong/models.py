from django.db import models
from django.utils.translation import gettext_lazy as _


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

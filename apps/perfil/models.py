from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import Voluntary
from ong.models import Project


class VoluntaryProjectJunction(models.Model):

    voluntary = models.ForeignKey(
        Voluntary, 
        verbose_name=_('voluntary'), 
        on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        Project, 
        verbose_name=_('project'), 
        on_delete=models.CASCADE
    )

    hours_worked = models.DecimalField(
        _('hours worked'), 
        max_digits=2, 
        decimal_places=2
    )

    approved = models.BooleanField(_("approved"), default=False)

    def __str__(self) -> str:
        return f'{self.voluntary.user.get_full_name()} : {self.project.title}'

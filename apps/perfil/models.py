from django.db import models
from authentication.models import Voluntary



class VoluntaryProjects(models.Model):

    project_name = models.CharField(max_length=30, blank=False)
    #TODO: AJUSTAR PARA PUXAR DOS PROJETOS ATIVOS
    hours_worked = models.IntegerField(blank=False)

    evidence_image = models.ImageField()

    voluntary = models.ForeignKey(Voluntary, on_delete=models.CASCADE)
    confirmation = models.BooleanField(default=False)
from django.db import models
from authentication.models import User



class VoluntaryProjects(models.Model):

    project_name = models.CharField(max_length=30, blank=False)
    hours_worked = models.IntegerField(blank=False)

    evidence_image = models.ImageField()

    voluntary = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation = models.BooleanField(default=False)
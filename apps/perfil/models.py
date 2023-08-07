from django.db import models



class VoluntaryProjects(models.Model):

    project_name = models.CharField(max_length=30, blank=False)
    hours_worked = models.IntegerField(blank=False)

    evidence_image = models.ImageField()

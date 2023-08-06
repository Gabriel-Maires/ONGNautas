from django.db import models
from authentication.validators import cep_validator

# Create your models here.
class Report(models.Model):

    title = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=300, blank=False)

    cep = models.CharField(max_length=11, blank=False, default='Sem CEP', validators=[cep_validator])
    address = models.CharField(max_length=64, blank=False, default='Não definido')
    complement = models.CharField(max_length=24, blank=True)

    evidence_image = models.ImageField()

    class Meta:
        verbose_name = 'Denúncia'
        verbose_name_plural = 'Denúncias'

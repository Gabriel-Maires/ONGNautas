from django.db import models
from authentication.validators import cep_validator


class Report(models.Model):

    title = models.CharField(max_length=30, blank=False)
    description = models.TextField()

    cep = models.CharField(max_length=8, blank=False, default='Sem CEP', validators=[cep_validator])
    address = models.CharField(max_length=64, blank=False, default='Não definido')
    complement = models.CharField(max_length=24, blank=True)

    evidence_image = models.ImageField(upload_to='denouncements')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Denúncia'
        verbose_name_plural = 'Denúncias'

from django.db import models

from .user import User


class Voluntary(models.Model):
    
    hours_worked = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

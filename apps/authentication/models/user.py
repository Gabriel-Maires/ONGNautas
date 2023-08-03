from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    is_voluntary = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False)
    cpf = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.get_full_name()

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from authentication.managers import UserManager

from authentication.validators import cpf_validator, cep_validator, no_whitespaces


class User(AbstractUser):

    username = models.CharField(max_length=150, blank=True, default='_')
    email = models.EmailField(
        _('email address'),
        unique=True, 
        blank=False, 
        validators=[no_whitespaces])
    first_name = models.CharField(
        _('first name'),
        max_length=32,
        blank=False,
        validators=[no_whitespaces]
    )
    last_name = models.CharField(
        _('last name'),
        max_length=32,
        blank=False,
        validators=[no_whitespaces]
    )

    is_voluntary = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False)
    cpf = models.CharField(max_length=11, blank=False, validators=[cpf_validator, no_whitespaces])
    birthdate = models.DateField(blank=False, default=timezone.now)
    cep = models.CharField(max_length=11, blank=False, default='Sem CEP', validators=[cep_validator, no_whitespaces])
    address = models.CharField(max_length=64, blank=False, default='Não definido')
    complement = models.CharField(max_length=24, blank=True)
     
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = list()

    objects: UserManager = UserManager()

    def __str__(self) -> str:
        return self.get_full_name()


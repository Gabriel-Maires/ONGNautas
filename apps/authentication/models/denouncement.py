from django.db import models

from .user import User

class Denouncement(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='denouncements')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
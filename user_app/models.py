from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True, max_length=128)
    password = models.CharField(max_length=256)
    username = models.CharField(blank=True, null=True, max_length=64, unique=True)

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class MyUser(AbstractUser):
    first_name = models.CharField(max_length=64, verbose_name='Imię')
    last_name = models.CharField(max_length=128, verbose_name='Nazwisko')
    email = models.EmailField(unique=True, max_length=128)
    password = models.CharField(max_length=256, verbose_name='Hasło')
    username = models.CharField(blank=True, null=True, max_length=64, unique=True)

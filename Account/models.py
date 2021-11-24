from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import EmailField
from .manager import *
# Create your models here.


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    fullname = models.CharField(max_length=150)
    contact = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    objects = UserManager()
    USERNAME_FIELD = 'contact'
    REQUIRED_FIELD = []

    def __str__(self):
        return self.fullname

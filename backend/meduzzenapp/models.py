from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    register_data = models.DateField("register data", auto_now_add=True)


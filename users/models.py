from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add additional fields or properties here if needed

    def __str__(self):
        return self.username

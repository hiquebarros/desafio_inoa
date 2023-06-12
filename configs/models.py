from django.db import models
from users.models import User

class Config(models.Model):
    stock_refresh_interval = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

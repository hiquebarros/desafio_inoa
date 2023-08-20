from django.db import models
from users.models import User

class Stock(models.Model):
    stock = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    logo = models.URLField()
    sector = models.CharField(max_length=100)

    def __str__(self):
        return self.stock
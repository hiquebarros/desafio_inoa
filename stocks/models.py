from django.db import models
from users.models import User

class Stock(models.Model):
    stock = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    close = models.FloatField()
    change = models.FloatField()
    volume = models.IntegerField()
    market_cap = models.BigIntegerField()
    logo = models.URLField()
    sector = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selling_price = models.FloatField()
    buying_price = models.FloatField()

    def __str__(self):
        return self.stock
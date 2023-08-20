from django.db import models
from users.models import User
from stocks.models import Stock

class StockUser(models.Model):
    close = models.FloatField()
    change = models.FloatField()
    volume = models.IntegerField()
    market_cap = models.BigIntegerField()
    selling_price = models.FloatField()
    buying_price = models.FloatField()
    is_notifying = models.IntegerField()
    update_perid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
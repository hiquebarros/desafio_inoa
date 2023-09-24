from django.db import models
from users.models import User
from stocks.models import Stock

class StockUser(models.Model):
    close = models.DecimalField(max_digits=10, decimal_places=8)
    change = models.DecimalField(max_digits=10, decimal_places=8)
    volume = models.IntegerField()
    market_cap = models.BigIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_notifying = models.IntegerField()
    update_period = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models
from users.models import User
from stocks.models import Stock
from django.utils import timezone

class StockUser(models.Model):
    close = models.DecimalField(max_digits=10, decimal_places=8)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_notifying = models.IntegerField()
    update_period = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    last_price_update = models.DateTimeField(default=timezone.now)
# stocks/urls.py
from django.urls import path
from .views import UserStocksView

app_name = 'stock_users'

urlpatterns = [
    path('<int:user_id>/', UserStocksView.as_view(), name='stock_users'),
]

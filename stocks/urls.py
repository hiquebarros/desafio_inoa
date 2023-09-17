# stocks/urls.py
from django.urls import path
from .views import StocksListView

app_name = 'stocks'

urlpatterns = [
    path('', StocksListView.as_view(), name='index'),
]

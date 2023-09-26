from django.shortcuts import render
from django.views.generic import ListView
from .models import Stock
from stock_users.models import StockUser
from users.models import User
import requests
from django.db.models import Subquery
from decimal import Decimal
from re import sub


class StocksListView(ListView):
    def get(self, request): 
        try:
            user = User.objects.get(pk=request.user.id)

            subquery = StockUser.objects.filter(user=user).values('stock_id')

            stocks = Stock.objects.exclude(pk__in=Subquery(subquery))
            
            return render(request, 'stocks/index.html', {'stocks': stocks})
        except User.DoesNotExist:
            return render(request, 'stocks/user_not_found.html')
    
    def post(self, request):

        user = User.objects.get(pk=request.user.id)
        subquery = StockUser.objects.filter(user=user).values('stock_id')
        stocks = Stock.objects.exclude(pk__in=Subquery(subquery))

        stock = request.POST.get('stock')
        selling_price = request.POST.get('selling_price')
        buying_price = request.POST.get('buying_price')
        is_notifying = request.POST.get('is_notifying')
        update_period = request.POST.get('update_period')
        stock = request.POST.get('stock')

        selling_price = Decimal(selling_price.replace(".", "").replace(",", "."))
        buying_price = Decimal(buying_price.replace(".", "").replace(",", "."))

        user_instance = User.objects.get(pk=request.user.id)
        stock_instance = Stock.objects.get(stock=stock)

        api_url = "https://brapi.dev/api/quote/list?sortBy=close&sortOrder=desc&limit=10&search={}".format(stock)
        
        try:
            response = requests.get(api_url)
            data = response.json()

            if(len(data['stocks']) < 1):
                raise Exception("A ação não está disponível no momento. Tente novamente mais tarde.")

            model_data = {
                "close": data['stocks'][0]['close'] if data['stocks'][0]['close'] else 0,
                "selling_price": selling_price, 
                "buying_price": buying_price,
                "is_notifying": is_notifying,
                "update_period": update_period,
                "user": user_instance,
                "stock": stock_instance,
            }

            stock_user_instance = StockUser(**model_data)
            stock_user_instance.save()
            
            stocks = Stock.objects.exclude(pk__in=Subquery(subquery))
            return render(request, 'stocks/index.html', {'stocks': stocks})

        except Exception as exception:
            return render(request, 'stocks/index.html', {'stocks': stocks, 'error_message': exception})
        
        

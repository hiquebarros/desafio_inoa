from django.shortcuts import render
from django.views.generic import ListView
from .models import Stock
from users.models import User

class StocksListView(ListView):
    def get(self, request): 
        try:
            user = User.objects.get(pk=request.user.id)
            stocks = Stock.objects.all()
            
            return render(request, 'stocks/index.html', {'stocks': stocks})
        except User.DoesNotExist:
            return render(request, 'stocks/user_not_found.html')

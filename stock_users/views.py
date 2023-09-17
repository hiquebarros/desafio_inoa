from django.shortcuts import render
from django.views import View
from users.models import User
from stock_users.models import StockUser

# Create your views here.

class UserStocksView(View):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            stock_users = StockUser.objects.filter(user_id=user_id)
            
            return render(request, 'stock_users/index.html', {'user': user, 'stocks': stock_users})
        except User.DoesNotExist:
            return render(request, 'user_not_found.html')
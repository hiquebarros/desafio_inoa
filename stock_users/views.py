from django.shortcuts import render
from django.views import View
from users.models import User
from stock_users.models import StockUser
from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponseRedirect
from django.urls import reverse


class UserStocksView(View):
    def get(self, request, user_id):

        user = request.user

        if not user.is_authenticated:
             return HttpResponseRedirect(reverse('users:login'))

        try:
            user = User.objects.get(pk=user_id)
            stock_users = StockUser.objects.filter(user_id=user_id)
            
            return render(request, 'stock_users/index.html', {'user': user, 'stocks': stock_users})
        except User.DoesNotExist:
            return render(request, 'user_not_found.html')
        
    def post(self, request):
            
            updated_stock_user_id = request.POST.get('updated_stock_user_id')

            if(updated_stock_user_id):
                 
                stock_user = StockUser.objects.get(pk=updated_stock_user_id)

                selling_price = request.POST.get('selling_price')
                buying_price = request.POST.get('buying_price')
                is_notifying = request.POST.get('is_notifying')
                update_period = request.POST.get('update_period')

                selling_price = Decimal(selling_price.replace(".", "").replace(",", "."))
                buying_price = Decimal(buying_price.replace(".", "").replace(",", "."))

                stock_user.selling_price = selling_price
                stock_user.buying_price = buying_price
                stock_user.is_notifying = is_notifying
                stock_user.update_period = update_period
                stock_user.save()

                return HttpResponseRedirect(reverse('stock_users:stock_users', args=[stock_user.user.id]))

            else:
                stock_user_id = request.POST.get('stock_user')
                stock_user = StockUser.objects.get(pk=stock_user_id)
                stock_user.delete()
                
                return HttpResponseRedirect(reverse('stock_users:stock_users', args=[stock_user.user.id]))
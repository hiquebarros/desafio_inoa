from django.core.management.base import BaseCommand
from stock_users.models import StockUser
import requests
from django.utils import timezone

class Command(BaseCommand):
    help = 'Script para atualizar ações do banco de dados.'

    def handle(self, *args, **options):

        stocks = []
        stock_users_list = []

        current_datetime = timezone.now()
        stock_users = StockUser.objects.all()

        for stock_user in stock_users:
            time_difference = current_datetime - stock_user.updated_at
            seconds = time_difference.seconds
            minutes = (seconds % 3600) // 60
            if (minutes >= stock_user.update_period):
                stocks.append(stock_user.stock.stock)
                stock_users_list.append(stock_user)

        stock_string = ",".join(stocks)
        api_url = f"https://brapi.dev/api/quote/{stock_string}"
        response = requests.get(api_url)

        data = None

        if response.status_code == 200:
            try:
                data = response.json()
            except ValueError:
                print("Não foram encontradas ações para atualização.")

        if data is not None:
            for stock_from_api in data['results']:
                for stock_user_instance in stock_users_list:
                    if(stock_user_instance.stock.stock == stock_from_api['symbol']):
                        Command.handleNotification(stock_user_instance, stock_from_api['regularMarketPrice'])

                        stock_user_instance.close = stock_from_api['regularMarketPrice']
                        stock_user_instance.save()


    def handleNotification(stock_user, newPrice):
        if(stock_user.is_notifying == False):
            return False
        
        if(newPrice >= stock_user.selling_price):
            Command.notify("sell")
        elif(newPrice <= stock_user.buying_price):
            Command.notify("buy")
        
    def notify(string):
        return print(string)

        
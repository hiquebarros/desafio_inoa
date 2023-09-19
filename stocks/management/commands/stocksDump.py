from django.core.management.base import BaseCommand
from stocks.models import Stock
import requests

class Command(BaseCommand):
    help = 'Script para popular tabela stocks.'

    def handle(self, *args, **options):
        api_url = "https://brapi.dev/api/quote/list?limit=10"

        try:
            response = requests.get(api_url)

            if response.status_code == 200:

                data = response.json()

                for item in data['stocks']:

                    stock_dict = {
                        'stock': item.get('stock', ''),
                        'name': item.get('name', ''),   
                        'logo': item.get('logo', ''),  
                        'sector': item['sector'] if item['sector'] is not None else 'Sem setor definido'
                    }

                    stock_instance = Stock(**stock_dict)
                    stock_instance.save() 

            else:
            
                print(f"HTTP request failed with status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

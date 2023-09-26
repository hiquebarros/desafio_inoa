from django.apps import AppConfig
from jobs import updater

class StockUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock_users'

    def ready(self):
    	updater.start()

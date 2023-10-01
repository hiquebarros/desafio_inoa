from django.core.management import call_command

def schedule_update():
    call_command('updateStocks')
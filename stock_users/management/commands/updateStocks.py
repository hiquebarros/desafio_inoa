from django.core.management.base import BaseCommand
from stock_users.models import StockUser
import requests
from django.utils import timezone
import smtplib
from email.message import EmailMessage
from jinja2 import Template

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

        if(len(stocks) > 0):
            stock_string = ",".join(stocks)
            api_url = f"https://brapi.dev/api/quote/{stock_string}"
            response = requests.get(api_url)
            data = None

            if response.status_code == 200:
                try:
                    data = response.json()
                    print(data['results'][0])
                except ValueError:
                    print("Não foram encontradas ações para atualização.")

            if data is not None:
                for stock_from_api in data['results']:
                    for stock_user_instance in stock_users_list:
                        if(stock_user_instance.stock.stock == stock_from_api['symbol']):
                            Command.handleNotification(stock_user_instance, stock_from_api['regularMarketPrice'])

                            stock_user_instance.close = stock_from_api['regularMarketPrice']
                            stock_user_instance.last_price_update = timezone.now()
                            stock_user_instance.save()


    def handleNotification(stock_user, newPrice):
        if(stock_user.is_notifying == False):
            return False
        
        if(newPrice >= stock_user.selling_price):
            Command.notifySell(stock_user)
        elif(newPrice <= stock_user.buying_price):
            Command.notifyBuy(stock_user)
        
    def notifyBuy(stock_user):

        EMAIL_ADDRESS = "inoateste@gmail.com"
        EMAIL_PASSWORD = "ejqm unah bznr mxak"

        html_template = '''
            <div class="container text-center mt-5">
                <div class="alert alert-success">
                    Olá {{ username }}! A ação <strong>{{ stock_name }}</strong> está dentro do preço de compra ideal para você.
                </div>
                <p class="mt-3">R$ {{ stock_close }}</p>
            </div>
        '''
        template = Template(html_template)
        rendered_html = template.render(
            stock_logo=stock_user.stock.logo,
            stock_close=float(stock_user.close),
            username=stock_user.user.username,
            stock_name=stock_user.stock.name
        )

        msg = EmailMessage()
        msg['Subject'] = "Notificação de monitoramento"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = stock_user.user.email
        msg.set_content(rendered_html, subtype='html')

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print("Email enviado com sucesso")
        except Exception as e:
            print("Erro ao enviar email:", str(e))

    def notifySell(stock_user):

        EMAIL_ADDRESS = "inoateste@gmail.com"
        EMAIL_PASSWORD = "ejqm unah bznr mxak"

        html_template = '''
            <div class="container text-center mt-5">
                <div class="alert alert-success">
                    Olá {{ username }}! A ação <strong>{{ stock_name }}</strong> está dentro do preço de venda ideal para você.
                </div>
                <p class="mt-3">R$ {{ stock_close }}</p>
            </div>
        '''

        template = Template(html_template)
        rendered_html = template.render(
            stock_logo=stock_user.stock.logo,
            stock_close=float(stock_user.close),
            username=stock_user.user.username,
            stock_name=stock_user.stock.name
        )

        msg = EmailMessage()
        msg['Subject'] = "Notificação de monitoramento"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = stock_user.user.email
        msg.set_content(rendered_html, subtype='html')

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print("Email enviado com sucesso")
        except Exception as e:
            print("Erro ao enviar email:", str(e))

        
# Generated by Django 4.2.2 on 2023-09-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_users', '0007_remove_stockuser_change_remove_stockuser_market_cap_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockuser',
            name='last_price_update',
            field=models.DateTimeField(null=True),
        ),
    ]

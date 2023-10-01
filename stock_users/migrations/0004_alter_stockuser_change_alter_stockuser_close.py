# Generated by Django 4.2.2 on 2023-09-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_users', '0003_alter_stockuser_buying_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockuser',
            name='change',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockuser',
            name='close',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_app', '0009_auto_20200330_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todays',
            name='price_data',
            field=models.CharField(max_length=64),
        ),
    ]

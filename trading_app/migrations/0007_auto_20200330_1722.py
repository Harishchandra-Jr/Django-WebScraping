# Generated by Django 3.0.4 on 2020-03-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_app', '0006_auto_20200330_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todays',
            name='Avgvol_In3Month',
            field=models.CharField(max_length=64),
        ),
    ]

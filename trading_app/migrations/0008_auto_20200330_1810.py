# Generated by Django 3.0.4 on 2020-03-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_app', '0007_auto_20200330_1722'),
    ]

    operations = [
        migrations.DeleteModel(
            name='abc',
        ),
        migrations.AlterField(
            model_name='todays',
            name='change',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='todays',
            name='company_name',
            field=models.CharField(max_length=64),
        ),
    ]

# Generated by Django 2.2.5 on 2021-04-20 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockApp', '0002_auto_20210416_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('market_cap', models.CharField(max_length=30)),
                ('time_stamp', models.TimeField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
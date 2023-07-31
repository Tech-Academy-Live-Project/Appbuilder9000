# Generated by Django 3.1.2 on 2020-12-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cbooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=300)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('images', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
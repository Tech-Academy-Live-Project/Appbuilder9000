# Generated by Django 2.2.5 on 2021-04-09 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuitarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('Acoustic', 'Acoustic'), ('Electro-Acoustic', 'Electro-Acoustic'), ('Electric', 'Electric'), ('Bass', 'Bass')], max_length=50)),
                ('stars', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])),
                ('review', models.TextField(max_length=2000)),
            ],
        ),
    ]
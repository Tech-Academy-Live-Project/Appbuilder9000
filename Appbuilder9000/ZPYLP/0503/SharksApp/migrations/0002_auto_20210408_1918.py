# Generated by Django 2.2.5 on 2021-04-09 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SharksApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharks',
            name='endangered',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='sharks',
            name='location',
            field=models.CharField(choices=[('Atlantic', 'Atlantic'), ('Pacific', 'Pacific'), ('Indian', 'Indian'), ('Arctic', 'Arctic')], max_length=50),
        ),
    ]
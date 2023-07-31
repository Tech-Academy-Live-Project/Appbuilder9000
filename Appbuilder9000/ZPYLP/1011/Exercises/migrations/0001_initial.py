# Generated by Django 2.2.5 on 2021-09-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_muscle', models.CharField(max_length=60)),
                ('exercise_name', models.CharField(blank=True, default='', max_length=60)),
                ('repetitions', models.IntegerField(max_length=2)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
            ],
        ),
    ]
# Generated by Django 2.2.5 on 2021-06-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=30)),
                ('Quote', models.CharField(max_length=1000)),
                ('Year', models.IntegerField()),
                ('subject', models.CharField(choices=[('CH', 'Cheerful'), ('RE', 'Reflective'), ('GL', 'Gloomy'), ('HU', 'Humorous'), ('ME', 'Melancholy'), ('ID', 'Idyllic'), ('WH', 'Whimsical'), ('RO', 'Romantic'), ('MY', 'Mysterious'), ('OM', 'Ominous'), ('CA', 'Calm'), ('LI', 'Lighthearted'), ('HO', 'Hopeful'), ('AN', 'Angry'), ('FinancialEvaluator', 'Fearful'), ('TE', 'Tense'), ('LO', 'Lonely'), ('IN', 'Inspirational')], max_length=50)),
            ],
        ),
    ]
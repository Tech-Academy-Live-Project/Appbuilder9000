# Generated by Django 2.2.5 on 2021-04-08 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_name', models.CharField(max_length=75)),
                ('word_def', models.CharField(max_length=255)),
                ('word_insent', models.CharField(max_length=255)),
                ('word_found', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='etymology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=255)),
                ('word_ety', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WordNerd.word')),
            ],
        ),
    ]
# Generated by Django 2.2.5 on 2021-01-25 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReflectiveJournal', '0014_posts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
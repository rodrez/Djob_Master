# Generated by Django 3.1.7 on 2021-03-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djob_profile', '0002_auto_20210318_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='availability',
            field=models.CharField(default='As soon as possible', max_length=150),
        ),
    ]

# Generated by Django 3.2 on 2021-05-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djob_jobs', '0008_auto_20210502_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='days_posted',
            field=models.DateField(default='05/04/2021'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-28 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djob_jobs', '0010_auto_20210505_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='days_posted',
            field=models.DateField(default='05/28/2021'),
        ),
    ]

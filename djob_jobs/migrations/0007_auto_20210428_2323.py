# Generated by Django 3.2 on 2021-04-29 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djob_jobs', '0006_auto_20210320_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_logo',
            field=models.ImageField(default='company_logos/default.png', upload_to='company_logos'),
        ),
        migrations.AlterField(
            model_name='job',
            name='days_posted',
            field=models.DateField(default='04/28/2021'),
        ),
    ]

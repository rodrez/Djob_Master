# Generated by Django 3.2 on 2021-05-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djob_jobs', '0007_auto_20210428_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='days_posted',
            field=models.DateField(default='05/02/2021'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_summary',
            field=models.TextField(default='Enter job description.'),
        ),
    ]

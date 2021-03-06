# Generated by Django 3.2.1 on 2021-05-05 21:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djob_jobs', '0009_alter_job_days_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='days_posted',
            field=models.DateField(default='05/05/2021'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_summary',
            field=ckeditor.fields.RichTextField(default='Enter job description.'),
        ),
    ]

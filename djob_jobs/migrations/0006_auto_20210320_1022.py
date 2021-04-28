# Generated by Django 3.1.7 on 2021-03-20 14:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djob_jobs', '0005_auto_20210319_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-days_posted']},
        ),
        migrations.AlterField(
            model_name='job',
            name='benefits',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='days_posted',
            field=models.DateField(default='03/20/2021'),
        ),
        migrations.AlterField(
            model_name='job',
            name='minimum_requirements',
            field=ckeditor.fields.RichTextField(default='Enter minimum requirements.'),
        ),
        migrations.AlterField(
            model_name='job',
            name='preferred_requirements',
            field=ckeditor.fields.RichTextField(blank=True, default='Enter minimum requirements.', null=True),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(blank=True, default='Default - Harvard', max_length=200, null=True)),
                ('degree', models.CharField(blank=True, default='Default - Engineering', max_length=150, null=True)),
                ('grad_date', models.CharField(blank=True, default='Default - 2021', max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, default='Default - Engineer', max_length=150, null=True)),
                ('time_at_job', models.CharField(blank=True, default='Default - 1 year', max_length=150, null=True)),
                ('job_location', models.CharField(blank=True, default='Default - Los Angeles', max_length=150, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(default='Enter something awesome about yourself.')),
                ('phone', models.CharField(blank=True, help_text='Contact phone number', max_length=15)),
                ('zipcode', models.CharField(default='17055', max_length=255)),
                ('location', models.CharField(blank=True, max_length=300, null=True)),
                ('current_job', models.CharField(default='Awesome Job', max_length=75, null=True)),
                ('employment_type', models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part-Time'), ('IT', 'Internship'), ('CT', 'Contract')], default='FT', max_length=2)),
                ('work_authorization', models.CharField(choices=[('UC', 'US Citizen'), ('CC', 'Canadian Citizen'), ('GC', 'Green Card Holder'), ('EA', 'Employment Auth Document'), ('NV', 'Need H1 Visa'), ('HV', 'have N1 Visa')], default='UC', max_length=2)),
                ('minimum_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('relocate', models.BooleanField(default=False)),
                ('travel', models.BooleanField(default=False)),
            ],
        ),
    ]

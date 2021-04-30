import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'Djob_Master.settings'
django.setup()

from djob_data.models import JobTitle, City

import re
import json

# JobTitle.objects.all().delete()
def jt():
    with open('jobs.txt', 'r') as f:
        title = f.readlines()
        job_titles = [re.sub('[^A-Za-z0-9/+\s]+', '', job).strip() for job in title]
        # job_titles.append([job for job in title if "in" not in title])
        return job_titles

def upload_titles():
    for j in jt():
        if j not in JobTitle.objects.values_list('title'):
            JobTitle.objects.create(title=j)

upload_titles()

def get_json_data():
    with open('../static/data/cities.json') as f:
        data = json.load(f)
    for i in data:
        City.objects.create(
            city=i['city'],
            zipcode=i['zip_code'],
            state=i['state'],
            latitude=i['latitude'],
            longitude=i['longitude']
        )
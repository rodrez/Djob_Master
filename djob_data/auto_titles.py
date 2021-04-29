import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'Djob_Master.settings'
django.setup()

from djob_data.models import JobTitle

import re

JobTitle.objects.all().delete()
def jt():
    with open('jobs.txt', 'r') as f:
        title = f.readlines()
        job_titles = [re.sub('[^A-Za-z0-9/+\s]+', '', job).strip() for job in title]
        # job_titles.append([job for job in title if "in" not in title])
        return job_titles


for j in jt():
    if j not in JobTitle.objects.values_list('title'):
        JobTitle.objects.create(title=j)


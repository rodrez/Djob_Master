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


def upload_titles(job_titles):
    for job in job_titles:
        if job not in JobTitle.objects.values_list('title'):
            JobTitle.objects.create(
                title=job[1].title(),
                category=job[0]
            )




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


def js_arr_to_list():
    with open('jobs.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            start = line.find('"') + 1
            stop = line.rfind('"')
            title = line[start:stop]
            print(title)


from bs4 import BeautifulSoup
import requests


def glassdoor_titles():
    # Titles
    URL = "https://www.glassdoor.com/sitedirectory/title-jobs.htm"
    main_url = 'https://www.glassdoor.com'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')
    cats = soup.select('.module > div:nth-child(2) > ul:nth-child(2) > li > a')

    links = [main_url+t['href'] for t in cats]
    categories = [t.text for t in cats]

    cat_and_titles = []

    for idx, link in enumerate(links):
        html = requests.get(link)
        link_text = BeautifulSoup(html.text, 'lxml')
        raw_titles = link_text.findAll('div', {'class': 'h3 strong'})
        titles = [title.text for title in raw_titles]
        for title in titles:
            cat_and_titles.append((categories[idx], title))

    return cat_and_titles
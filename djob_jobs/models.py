from django.db import models
import datetime
from ckeditor.fields import RichTextField

from Djob_Master import settings


# Create your models here.


class Tags(models.Model):
    tag = models.CharField(max_length=70)

    def __str__(self):
        return self.tag


class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # TODO: Work on dynamically adding more tags

    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    apply = models.CharField(max_length=1000)
    job_summary = RichTextField(default="Enter job description.")
    minimum_requirements = RichTextField(default="Enter minimum requirements.")
    preferred_requirements = RichTextField(default="Enter preferred requirements.", blank=True, null=True)
    benefits = RichTextField(blank=True, null=True)
    salary_range = models.CharField(blank=True, null=True, max_length=30)
    days_posted = models.DateField(auto_now_add=True)
    company_logo = models.ImageField(upload_to="company_logos",
                                     default='company_logos/default.png')
    tags = models.ManyToManyField(Tags, blank=True)


    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ["-days_posted"]

        # permissions = [
        #     ('employer', 'Can post new jobs'),
        # ]


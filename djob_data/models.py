from django.db import models

# Create your models here.
class JobTitle(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class City(models.Model):

    city = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=6)
    state = models.CharField(max_length=200)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)

    def __str__(self):
        return self.city
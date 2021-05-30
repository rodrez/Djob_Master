from ckeditor.fields import RichTextField
from django.db import models
from Djob_Master import settings
from django_quill.fields import QuillField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profiles')
    summary = RichTextField(default="Enter something awesome about yourself.")
    phone = models.CharField(max_length=15, blank=True, help_text='Contact phone number')
    zipcode = models.CharField(max_length=255, default='17055')
    location = models.CharField(max_length=300, null=True, blank=True)


    EMPLOYMENT_TYPES = (
        ("FT", "Full Time"),
        ("PT", "Part-Time"),
        ('IT', "Internship"),
        ('CT', "Contract"),
    )
    current_job = models.CharField(max_length=75, null=True, default="Awesome Job")
    employment_type = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_TYPES,
        default="FT",
    )

    WA = (
        ('UC', "US Citizen"),
        ('CC', "Canadian Citizen"),
        ('GC', "Green Card Holder"),
        ('EA', "Employment Auth Document"),
        ('NV', "Need H1 Visa"),
        ('HV', "have N1 Visa")
    )

    work_authorization = models.CharField(
        max_length=2,
        choices=WA,
        default="UC",
    )
    availability = models.CharField(default="As soon as possible", max_length=150)
    minimum_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    relocate = models.BooleanField(default=False)
    travel = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username.capitalize()} Profile | ID-{self.id}'


class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution = models.CharField(default='Default - Harvard', max_length=200, null=True, blank=True)
    degree = models.CharField(default='Default - Engineering', max_length=150, null=True, blank=True)
    grad_date = models.CharField(default='Default - 2021', max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username.capitalize()} Education'


class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_title = models.CharField(default='Default - Engineer', max_length=150, null=True, blank=True)
    time_at_job = models.CharField(default='Default - 1 year', max_length=150, null=True, blank=True)
    job_location = models.CharField(default='Default - Los Angeles', max_length=150, null=True, blank=True)
    job_description = QuillField()

    def __str__(self):
        return f'{self.user.username.capitalize()} Experience'
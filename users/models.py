from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    RECRUITER = 'recruiter'
    CANDIDATE = 'candidate'

    role = models.CharField(max_length=20, choices=[(RECRUITER, 'Recruiter'), (CANDIDATE, 'Candidate')])

    def get_profile(self):
        return self.profiles.id
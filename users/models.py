from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def get_profile(self):
        return self.profiles.id
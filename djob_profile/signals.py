from django.db.models.signals import post_save
from django.dispatch import receiver

from Djob_Master import settings
from .models import Profile, Experience, Education


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Args:
        sender:
        instance:
        created:
        **kwargs:
    """
    if created:
        Profile.objects.create(user=instance)
        Experience.objects.create(user=instance)
        Education.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Args:
        sender:
        instance:
        **kwargs:
    """
    instance.profiles.save()

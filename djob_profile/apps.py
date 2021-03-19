from django.apps import AppConfig


class DjobProfileConfig(AppConfig):
    name = 'djob_profile'

    def ready(self):
        import djob_profile.signals
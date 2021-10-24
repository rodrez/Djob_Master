from django.urls import path
from rest_framework import routers
from .views import (
    UserViewSet,
    JobViewSet,
    ProfileViewSet,
    EducationViewSet, 
    ExperienceViewSet
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'jobs', JobViewSet, basename='jobs')
router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'educations', EducationViewSet, basename='educations')
router.register(r'experiences', ExperienceViewSet, basename='experiences')

urlpatterns = router.urls
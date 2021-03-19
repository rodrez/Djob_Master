from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView, EducationFormView, ExperienceFormView

urlpatterns = [
    path('<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/edit', ProfileUpdateView.as_view(), name='profile_update'),
    path('<int:pk>/edit_experience', ExperienceFormView.as_view(), name='update_exp'),
    path('<int:pk>/edit_education', EducationFormView.as_view(), name='update_edu'),
]

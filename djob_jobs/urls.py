from django.urls import path

from .views import JobDetailView, JobPostView, JobEditView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('job/<pk>/', JobDetailView.as_view(), name="job-detail"),
    path('job-post/', login_required(JobPostView.as_view()), name="job-post"),
    path('job/<pk>/edit/', login_required(JobEditView.as_view()), name="job-edit"),
]

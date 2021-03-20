from django.urls import path

from .views import JobDetailView, JobPostView, JobEditView, JobDeleteView, JobListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', JobListView.as_view(), name="jobs"),
    path('job/<pk>', JobDetailView.as_view(), name="job-detail"),
    path('job-post/', login_required(JobPostView.as_view()), name="job-post"),
    path('job/<pk>/edit/', login_required(JobEditView.as_view()), name="job-edit"),
    path('job/delete/<pk>/', csrf_exempt(JobDeleteView.as_view()), name="job-delete"),
]

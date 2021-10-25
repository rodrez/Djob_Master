from rest_framework import viewsets
from django.contrib.auth import get_user_model
from djob_jobs.models import Job
from djob_profile.models import Profile, Education, Experience


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.social_serializers import TwitterLoginSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import (
    JobSerializer,
    ProfileSerializer,
    EducationSerializer,
    ExperienceSerializer,
    UserSerializer,
)

User = get_user_model()



class MyObtainToken(ObtainAuthToken):
    """Return User Info along with token"""

    def post(self, request, *args, **kwargs):

        response = super(MyObtainToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response(
            {
                "token": token.key,
                "id": token.user_id,
                "email": token.user.email,
                "first_name": token.user.first_name,
                "last_name": token.user.last_name,
            }
        )



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Custom query set for User model
    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    # Custom queryset for the viewset
    def get_queryset(self):
        queryset = Job.objects.all()

        if not self.request:
            return JobSerializer.objects.none()

        # Filter by the title
        title = self.request.query_params.get("title", None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        # Filter by the location
        location = self.request.query_params.get("location", None)
        if location is not None:
            queryset = queryset.filter(location__icontains=location)

        # Filter by the tag
        tag = self.request.query_params.get("tag", None)
        if tag is not None:
            queryset = queryset.filter(tags__icontains=tag)

        # Filter by the company
        company = self.request.query_params.get("company", None)
        if company is not None:
            queryset = queryset.filter(company__icontains=company)

        return queryset


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # Custom queryset for the viewset
    def get_queryset(self):
        queryset = Profile.objects.all()

        if not self.request:
            return ProfileSerializer.objects.none()

        # Filter by the location
        location = self.request.query_params.get("location", None)
        if location is not None:
            queryset = queryset.filter(location__icontains=location)

        # Filter by availability
        availability = self.request.query_params.get("availability", None)
        if availability is not None:
            queryset = queryset.filter(availability__icontains=availability)

        # Filter by travel
        travel = self.request.query_params.get("travel", None)
        if travel is not None:
            queryset = queryset.filter(travel__icontains=travel)

        # Filter by relocate
        relocate = self.request.query_params.get("relocate", None)
        if relocate is not None:
            queryset = queryset.filter(relocate__icontains=relocate)

        return queryset


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    # Custom queryset for the viewset
    def get_queryset(self):
        queryset = Education.objects.all()

        if not self.request:
            return EducationSerializer.objects.none()

        # Filter by the degree
        degree = self.request.query_params.get("degree", None)
        if degree is not None:
            queryset = queryset.filter(degree__icontains=degree)

        return queryset


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    # Custom queryset for the viewset
    def get_queryset(self):
        queryset = Experience.objects.all()

        if not self.request:
            return ExperienceSerializer.objects.none()

        # Filter by the job description
        job_description = self.request.query_params.get("job_description", None)
        if job_description is not None:
            queryset = queryset.filter(job_description__icontains=job_description)

        return queryset

# Social Login  

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
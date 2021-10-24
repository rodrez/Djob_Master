from rest_framework import serializers
from djob_jobs.models import Job
from djob_profile.models import Profile, Education, Experience
from django.contrib.auth import get_user_model

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


# Job serializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


# Profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


# Education serializer
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


# Experience serializer
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


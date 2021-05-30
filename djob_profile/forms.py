from django.forms.models import ModelForm, modelformset_factory

from .models import Profile, Education, Experience


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['summary', 'location', 'minimum_salary', 'employment_type', 'work_authorization', 'relocate',
                  'travel', 'relocate', 'phone', 'current_job']


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            'institution', 'degree', 'grad_date', 'id'
        ]


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            'job_title', 'job_description', 'job_location', 'time_at_job', 'id'
        ]


EducationFormSet = modelformset_factory(Education, exclude=(), extra=0, can_delete=True)
ExperienceFormSet = modelformset_factory(Experience, exclude=(), extra=0, can_delete=True)

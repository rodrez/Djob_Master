from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, FormView

from users.forms import CustomUserForm
from users.models import User
from .forms import ProfileForm, ExperienceFormSet, EducationFormSet
from .models import Profile, Education, Experience


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'djob_profile/profile.html'
    context_object_name = 'profile'
    fields = ['summary', 'location', 'minimum_salary', 'employment_type', 'work_authorization', 'relocate',
              'travel', 'relocate', 'phone', 'current_job']


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'djob_profile/profile_edit.html'
    model = Profile
    form_classes = ProfileForm

    fields = ['summary', 'location', 'minimum_salary', 'employment_type', 'work_authorization', 'relocate',
              'travel', 'relocate', 'phone', 'current_job']

    def get_second_form(self):
        # logic to construct second form goes here
        # if self.request.method == 'POST' you need to pass self.request.POST
        # to the form. Add whatever you need to create the form
        context = {}
        if self.request.method == 'POST':
            obj = User.objects.get(pk=self.request.user.pk)
            # edu = Education.objects.get(user_id=self.request.user.id)

            form = CustomUserForm(initial={
                'first_name': obj.first_name,
                'last_name': obj.last_name,
                'email': obj.email})

            context['user'] = form
            # context['edu'] = edu

            return context
        else:
            return CustomUserForm()

    def form_valid(self, form):

        """
        Args:
            form:
        """
        if self.request.method == 'POST':

            self.object.maker = Profile.objects.get(pk=self.request.user.pk)

            # Grabs the data from the form with the POST method
            fn = self.request.POST.get('first_name')
            ln = self.request.POST.get('last_name')
            em = self.request.POST.get('email')

            # Loads the second form and updates the database with the form data
            obj = User.objects.get(pk=self.request.user.pk)
            obj.email = em
            obj.first_name = fn
            obj.last_name = ln
            obj.save()

            form.save()

            return super(ProfileUpdateView, self).form_valid(form)
        else:
            return redirect(self.get_success_url())

    def form_invalid(self, **kwargs):
        """
        Args:
            **kwargs:
        """
        return self.render_to_response(self.get_context_data(**kwargs))

    def get_success_url(self):
        return reverse_lazy('profile', args=[self.object.id])

    def get_context_data(self, **kwargs):
        """
        Args:
            **kwargs:
        """
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)

        # Gets the data from the current user
        user_obj = User.objects.get(pk=self.request.user.pk)

        # applies initial data to the form
        # This is necessary so the form doesn't show up blank.
        user_form = CustomUserForm(initial={
            'first_name': user_obj.first_name,
            'last_name': user_obj.last_name,
            'email': user_obj.email
        })

        context['user_form'] = user_form
        return context


class EducationFormView(LoginRequiredMixin, FormView):
    template_name = 'djob_profile/education_update.html'
    form_class = EducationFormSet

    def get_success_url(self):
        return reverse_lazy('profile', args=[self.request.user.id])

    def get_context_data(self, **kwargs):
        """
        Args:
            **kwargs:
        """
        context = super(EducationFormView, self).get_context_data(**kwargs)

        context['profile'] = Profile.objects.get(id=self.request.user.pk)
        context['experience'] = ExperienceFormSet(queryset=Experience.objects.filter(user=self.request.user.id))

        edu_nums = Education.objects.filter(user_id=self.request.user.id).count()

        if edu_nums:
            context['form'] = EducationFormSet()
        context['form'] = EducationFormSet(queryset=Education.objects.filter(user=self.request.user.id))
        return context

    def form_valid(self, form):

        """
        Args:
            form:
        """
        print(form.model)

        if form.is_valid():
            # form.data['user'] = self.request.user

            form.save()
        return super(EducationFormView, self).form_valid(form)


class ExperienceFormView(LoginRequiredMixin, FormView):
    template_name = 'djob_profile/experience_update.html'
    form_class = ExperienceFormSet
    model = Profile

    def get_success_url(self):
        return reverse_lazy('profile', args=[self.request.user.id])

    def get_context_data(self, **kwargs):
        """
        Args:
            **kwargs:
        """
        context = super(ExperienceFormView, self).get_context_data(**kwargs)

        context['profile'] = Profile.objects.get(id=self.request.user.get_profile())
        exp_nums = Experience.objects.filter(user_id=self.request.user.id).count()
        print(exp_nums)

        if exp_nums:
            context['form'] = ExperienceFormSet()
        context['form'] = ExperienceFormSet(queryset=Experience.objects.filter(user=self.request.user.id))
        return context

    def form_valid(self, form):
        """
        Args:
            form:
        """
        if form.is_valid():
            form.save()
        return super(ExperienceFormView, self).form_valid(form)

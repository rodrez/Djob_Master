from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .forms import JobForm
from .models import Job


class JobDetailView(DetailView):
    # specify the model to use
    model = Job
    template_name = 'djob_jobs/job_detail.html'


class JobPostView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'djob_jobs/job_post.html'
    context_object_name = 'job_post'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobPostView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('jobs')


class JobEditView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'djob_jobs/job_edit.html'

    def get_success_url(self):
        return reverse_lazy('job-detail', args=[self.object.id])

    def form_valid(self, form):
        return super(JobEditView, self).form_valid(form)


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job

    def get_success_url(self):
        return reverse_lazy('jobs')

class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'djob_jobs/job_list.html'
    context_object_name = 'jobs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)

        context['jobs'] = Job.objects.filter(user_id=self.request.user.id)

        return context

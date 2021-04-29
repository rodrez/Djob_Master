import json

from django.views.generic import ListView

from djob_data.models import JobTitle
from djob_jobs.models import Job





# Create your views here.
class HomeListView(ListView):

    template_name = "pages/home.html"
    model = Job
    context_object_name = 'job_list'
    paginate_by = 15
    queryset = Job.objects.order_by('-days_posted')
    
    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(HomeListView, self).get_context_data(**kwargs)
        j_titles = [name[0] for name in list(JobTitle.objects.values_list("title"))]
        context['job_titles'] = j_titles


        return context
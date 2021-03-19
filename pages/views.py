from django.views.generic import ListView

from djob_jobs.models import Job


# Create your views here.
class HomeListView(ListView):

    template_name = "pages/home.html"
    model = Job
    context_object_name = 'job_list'
    paginate_by = 15
    queryset = Job.objects.order_by('-days_posted')

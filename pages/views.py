from django.views.generic import ListView

from djob_data.models import JobTitle, City
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

        cities_name = [c[0] for c in list(City.objects.values_list("city"))]
        context['city'] = cities_name

        zips = [c[0] for c in list(City.objects.values_list("zipcode"))]
        context['zipcode'] = zips

        lats = [c[0] for c in list(City.objects.values_list("latitude"))]
        context['latitude'] = lats

        long = [c[0] for c in list(City.objects.values_list("longitude"))]
        context['longitude'] = long

        states = [c[0] for c in list(City.objects.values_list("state"))]
        context['state'] = states

        return context
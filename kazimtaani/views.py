from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Location, Poster,Category, Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    categories = Category.objects.all()
    location = request.GET.get('location')
    if location ==None:
        jobs = Job.objects.all()
    else:
        jobs = Job.objects.filter(location__location=location)
    locations = Location.objects.all()
    context = {'jobs':jobs, 'categories':categories, 'locations':locations}
    return render(request,'index.html', context)

def job(request,job_id):
    try:
        job = Job.objects.get(id= job_id)
    except:
        raise Http404()
    return render(request,'job.html',{'job':job})

def search_results(request):

    if 'job' in request.GET and request.GET["job"]:
        search_term = request.GET.get("job")
        searched_jobs = Job.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"jobs": searched_jobs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
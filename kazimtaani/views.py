from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from django.contrib.auth.models import User
from .models import Location,Category, Job
from django.contrib.auth.decorators import login_required
from .forms import PostForm,LocationForm
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    jobs = Job.objects.all()
    categories = Category.objects.all()
    location = request.GET.get('location')
    locations = Location.objects.all()
    if location ==None:
        jobs = Job.objects.all()
    else:
        jobs = Job.objects.filter(location__location=location)
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
    
@login_required   
def NewPost(request):
    user = Profile.objects.get(user=request.user)
    if request.method == "POST":
        pf_form=PostForm(request.POST, request.FILES, user=user.id)
        l_form=LocationForm(request.POST)
        if pf_form.is_valid() and l_form.is_valid():
            pf_form.save()
            l_form.save()
            
            return redirect('index')
    else:
        pf_form=PostForm(user=user.id)
        l_form=LocationForm()

    context = {
                'pf_form':pf_form,
                'l_form':l_form
            }

    return render(request, 'post.html',context)




class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['title', 'description', 'category', 'location', 'siteurl', 'jobtype']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ['title', 'description', 'category', 'location', 'siteurl', 'jobtype']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.poster:
            return True
        return False


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = '/'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.poster:
            return True
        return False



class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['location']

    def form_valid(self, form):
        return super().form_valid(form)


class LocationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Location
    fields = ['location']

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


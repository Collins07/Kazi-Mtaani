from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import JobCreateView, LocationCreateView

urlpatterns =[
    path('',views.index,name='index'),
    path('job/<job_id>',views.job,name='job'),
    path('search/', views.search_results, name='search_results'),
    path('newpost', views.NewPost, name='newpost'),
    path('job/new/', JobCreateView.as_view(), name='job-create'),
    path('location/new/', LocationCreateView.as_view(), name='location-create'),
    
]
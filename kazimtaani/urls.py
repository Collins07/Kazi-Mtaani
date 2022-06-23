

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import JobCreateView, LocationCreateView, CategoryCreateView, JobUpdateView, JobDeleteView

urlpatterns =[
    path('',views.index,name='index'),
    path('job/<job_id>',views.job,name='job'),
    path('search/', views.search_results, name='search_results'),
    
    # New Posts 
    path('job/new/', JobCreateView.as_view(), name='job-create'),
    path('location/new/', LocationCreateView.as_view(), name='location-create'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),

    # Update Views
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    
]
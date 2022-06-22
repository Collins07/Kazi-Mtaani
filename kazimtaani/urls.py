from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.index,name='index'),
    path('job/<job_id>',views.job,name='job'),
    path('search/', views.search_results, name='search_results'),
    path('newpost', views.NewPost, name='newpost'),
    
]
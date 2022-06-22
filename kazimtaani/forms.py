from django import forms
from django.forms import ModelForm, widgets
from .models import Job


class PostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description','category', 'location', 'jobtype','siteurl']
from django import forms
from django.forms import ModelForm, widgets
from .models import Job,Location


class PostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description','category','jobtype','siteurl']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location'] 
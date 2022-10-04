from django import forms
from django.forms import ModelForm
from .models import *


class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = "__all__"



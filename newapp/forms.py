from django import forms
# from django.forms import ModelForm
from .models import *


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'




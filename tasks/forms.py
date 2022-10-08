from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
        # fields = ['name']
from django import forms
from django.forms import ModelForm
from .models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
        # fields = ['name']
        
class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = '__all__'
        widgets = {
            'startdate': DateInput(), # default date-format %m/%d/%Y will be used
            'enddate': DateInput() # specify date-frmat
        }

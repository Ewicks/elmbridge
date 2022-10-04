from django.shortcuts import render, redirect
from .forms import *
from .models import *


def home(request):
    person = Person.objects.all
    context = {
        'person': person
    }
    return render(request, 'newapp/home.html', context)


def join(request):
    if request.method == 'POST':
        form = PersonForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            return render(request, 'newapp/join.html', {'form': form, 'fname': fname})
        return redirect('home')
    else:
        form = PersonForm()
        return render(request, 'newapp/join.html', {'form': form})




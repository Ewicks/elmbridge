from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse


def home(request):
    jobs = Job.objects.all()
    form = JobForm()

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request, 'crudapp/home.html', {'jobs': jobs, 'form': form})


def edit(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'crudapp/edit.html', {'form': form})


def delete(request, pk):
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('home')
    return render(request, 'crudapp/delete.html', {})
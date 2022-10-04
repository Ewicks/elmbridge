from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    jobs = Job.objects.all()
    form = JobForm()

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'jobs': jobs, 'form': form}
    return render(request, 'crudapp/home.html', context)

# def index(request):
# 	tasks = Task.objects.all()
# 	form = TaskForm()

# 	if request.method =='POST':
# 		form = TaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('list')

# 	context = {'tasks':tasks, 'form':form}
# 	return render(request, 'tasks/list.html', context)
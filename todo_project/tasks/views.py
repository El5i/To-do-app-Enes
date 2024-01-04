from django.shortcuts import render

# Create your views here.
# In tasks/views.py
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    return render(request, 'tasks/home.html')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/create_task.html', {'form': form})

def uncompleted_tasks(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'title': 'Uncompleted Tasks'})

def completed_tasks(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'title': 'Completed Tasks'})

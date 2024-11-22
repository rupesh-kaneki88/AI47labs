from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Only show tasks for the logged-in user
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def home(request):
    if request.user.is_authenticated:
        return redirect('task_list')  # Redirect to the task list or main page
    return render(request, 'account/login_page.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(
            title=title,
            description=description,
            user=request.user  
        )
        return redirect('task_list')
    return render(request, 'tasks/create_task.html')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})

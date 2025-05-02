from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from .models import *
from .forms import *

def task_list(request):
    status = request.GET.get('status', '')
    deadline_filter = request.GET.get('deadline', '')

    tasks = Task.objects.filter(assignee = request.user)
    
    if status:
        tasks = tasks.filter(status=status)
    
    today = timezone.now().date()
    if deadline_filter == 'today':
        tasks = tasks.filter(deadline__date=today)
    elif deadline_filter == 'week':
        tasks = tasks.filter(deadline__date__lte=today + timedelta(days=7))
    elif deadline_filter == 'overdue':
        tasks = tasks.filter(deadline__date__lt=today)

    tasks = tasks.order_by('deadline')

    status_choice= Task.STATUS_CHOICES
    deadline_choice = (
        ('today', 'Today'),
        ('week', 'Week'),
        ('overdue', 'Overdue'),
    )
    context = {
        'tasks': tasks,
        'status_choice': status_choice,
        'deadline_choice': deadline_choice,
        'current_status': status,
        'current_deadline': deadline_filter,
        }
    
    return render(request, 'tasks/task_list.html', context )

def task_create(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assignee =request.user
            task.save()
            return redirect('task-list')
    
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, assignee=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, assignee=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'tasks/task_delete.html', {'task': task})

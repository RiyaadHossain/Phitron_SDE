from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

def show_task(req):
    tasks = TaskModel.objects.all()
    return render(req, 'show_task.html', {'tasks':tasks})

def add_task(req):
    context = dict()

    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task_page')
        context['form'] = form
        return render(req, 'add_task.html', context)

    context['form'] = TaskForm()
    return render(req, 'add_task.html', context)

def edit_task(req,id):
    context = dict()
    task = TaskModel.objects.get(pk=id)

    if req.method == 'POST':
        form = TaskForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task_page')
        context['form'] = form
        return render(req, 'add_task.html', context)

    context['form'] = TaskForm(instance=task)
    return render(req, 'add_task.html', context)

def delete_task(req,id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_task_page')
    
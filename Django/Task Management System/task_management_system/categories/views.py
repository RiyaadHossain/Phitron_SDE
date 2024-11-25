from django.shortcuts import render, redirect
from .forms import CategoryForm

def add_category(req):
    context = dict()

    if req.method == 'POST':
        form = CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        context['form'] = form
        return render(req, 'add_category.html', context)

    context['form'] = CategoryForm()
    return render(req, 'add_category.html', context)
from django.shortcuts import render,redirect
from form_app.models import StudentModel
from . import forms

def home(req):
    form = forms.StudentForm()
    if req.method == 'POST':
        form = forms.StudentForm(req.POST)
        if form.is_valid():
            form.full_clean()
            form.save()
        return render(req, 'home.html', {'form': form})
        
    return render(req, 'home.html', {'form': form})

def get_students(req):
    students = StudentModel.objects.all()
    return render(req, 'students.html', {'students': students})

def delete_student(req, roll):
    StudentModel.objects.get(pk=roll).delete()
    return redirect('homepage')
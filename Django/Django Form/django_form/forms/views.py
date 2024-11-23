from django.shortcuts import render
from . import forms

def bootstarp_form(req):
    return render(req, 'bootstarp_form.html')

def built_in_form(req):

    form = forms.DjangoFrom()

    # If want to access in the curr page
    if req.method == 'POST':
        form = forms.DjangoFrom(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # email = form.cleaned_data["email"]
            # password = form.cleaned_data["password"]

        return render(req, 'built_in_form.html', {'form':form})

    return render(req, 'built_in_form.html', {'form':form})

def file_upload(req):
    if req.method == 'POST':
        form = forms.UploadFile(req.POST, req.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./forms/uploads/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        return render(req, 'file_upload.html', {'form':form}) 
    else:
        form = forms.UploadFile()
    return render(req, 'file_upload.html', {'form':form}) 

def form_attr_widget(req):
    form = forms.Attr_Widget()

    if req.method == 'POST':
        form = forms.Attr_Widget(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(req, 'form_attr_widget.html', {'form': form})

    return render(req, 'form_attr_widget.html', {'form': form})

def form_validation(req):
    form = forms.Form_Validation()

    if req.method == 'POST':
        form = forms.Form_Validation(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(req, 'form_validation.html', {'form': form})

    return render(req, 'form_validation.html', {'form': form})

def form_field(req):
    return render(req, 'form_field.html')

# Built-in Form
def view_data(req):

    data = {'email': 'None', 'password': 'None'}
    if req.method == 'POST':
        form = forms.DjangoFrom(req.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            data['email'] = email
            data['password'] = password
            return render(req, 'view_data.html', {'data':data})

    return render(req, 'view_data.html', {'data':data})

# Bootstarp
# def view_data(req):
#     if req.method == 'POST':
#         email = req.POST.get('email')
#         password = req.POST.get('password')
#         data ={}
#         data['email'] =email
#         data['password'] =password
#     return render(req, 'view_data.html', {'data':data})

from django.shortcuts import render

def contact(req):
    return render(req, 'contact.html')

def about(req):
    return render(req, 'about.html')


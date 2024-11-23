from django.http import HttpResponse
from django.shortcuts import render


def about(req):
    return HttpResponse("This is about page")

def home(req):
    return render(req, 'index.html')
from django.shortcuts import render

def home(req):
    print(req.user)
    return render(req, 'index.html')
from django.shortcuts import render

def home(req):
    return render(req, 'home.html')

def page(req,id):
    # req.GET
    # print(id)
    return render(req, 'page.html')
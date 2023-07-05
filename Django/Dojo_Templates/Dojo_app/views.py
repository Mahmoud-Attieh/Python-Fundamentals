from django.shortcuts import render, redirect
from . import models



def index(request):
    context= {
        "select_dojo" : models.display(),
        "select_ninja" : models.show()
    }
    return render(request,'index.html', context)

def createdojo(request):
    models.createDojo(request)
    return redirect('/')

def createninja(request):
    models.createNinja(request)
    return redirect('/')

def display(request):
    return redirect('/')

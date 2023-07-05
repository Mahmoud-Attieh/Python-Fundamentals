from django.shortcuts import render

def index (request):
    context ={
        "name":"mahmmoud"
        
    }
    return render(request,'index.html',context)

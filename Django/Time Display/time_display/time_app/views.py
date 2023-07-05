from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "date" : strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    con = {
        "dat" : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    }
    return render(request, 'index.html', context , con)

def index(request ):
    con = {
        "dat" : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    }
    return render(request, 'index.html', con)

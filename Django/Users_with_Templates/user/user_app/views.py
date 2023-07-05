from django.shortcuts import render, redirect
from .models import User

def index(request):
    context = {
        "data" : User.objects.all()
    }
    return render(request, "index.html", context)


def run(request):
    if request.method == 'POST':
        first_name = request.POST['first'],
        last_name = request.POST['last'],
        email_address = request.POST['email'],
        age = request.POST['age'],
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            age=age
        )
    return redirect('index')
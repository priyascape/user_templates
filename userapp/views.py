
from django.shortcuts import render,redirect, HttpResponse
from .models import *




# Create your views here.

def index(request):
    context = {
        "users":User.objects.all()
    }
    return render(request, "index.html", context)



def create_user(request):
    print(request.POST)
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        age = int(request.POST['age'])
    )
    return redirect ('/')
    

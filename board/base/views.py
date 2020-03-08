from django.shortcuts import render
from base import views

# Create your views here.

def inicio(request):
    return render(request,'base.html')
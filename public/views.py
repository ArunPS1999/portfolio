from django.shortcuts import render,redirect
from django.http import HttpResponse



def userhome(request):
    return render(request,"data.html")


# Create your views here.

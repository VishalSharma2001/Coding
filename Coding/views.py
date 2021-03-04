from django.shortcuts import render
from django.http import HttpResponse
import os

def Home(request):
    return render(request,"index.html")
# def Coding(request):
#     return render(request,"Coding.html")
def Questions(request):
    return render(request,"Questions.html")
def ContactUs(request):
    return render(request,"ContactUs.html")
def About(request):
    return render(request,"About.html")
   



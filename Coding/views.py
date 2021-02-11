from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("This is my Official Website")
def add(request):
    return HttpResponse("This is my add")


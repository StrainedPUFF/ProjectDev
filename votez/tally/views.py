from django.shortcuts import render

# Create your views here.
from django .http import HttpResponse

def index(request):
    return HttpResponse("hello , Am Wesley and this is my first personal project.")
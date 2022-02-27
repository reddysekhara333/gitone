from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('hello welome to  git hub home page')
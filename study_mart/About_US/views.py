from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def about(request):
    return HttpResponse('<p>this is about our project </p>')

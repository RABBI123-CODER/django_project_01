from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def blog1(request):
    return HttpResponse('<p>this is our first blog </p>')

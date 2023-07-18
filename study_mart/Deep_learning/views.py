from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def deep_lear(request):
    return HttpResponse('<p>this is our first deep_learning </p>')

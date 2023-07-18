from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def machine_learning(request):
    return HttpResponse('<h1>studymart offering lots of free & paid course</h1>')


def deep_learning(request):
    return HttpResponse('<h1>this is deep learnig</h1>')


def about_us1(request):
    return HttpResponse('<h1>this is about us ..</h1>')

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def data_ana(request):
    return HttpResponse('p>this is our data_analysis project </p>')

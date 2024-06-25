from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def predicts(request):
    return HttpResponse( render(request, 'predicts.html' ))

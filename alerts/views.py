from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello, World!")

def alerts(request):
    #return alerts view
    return HttpResponse( render(request, 'alerts.html' ))

def base(request):
    #return alerts view
    return HttpResponse( render(request, 'base.html' ))
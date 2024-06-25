# neuronalTrade/views.py

from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return HttpResponse( render(request, 'base.html' ))


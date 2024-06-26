from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def alerts(request):
    return HttpResponse( render(request, 'alerts/alerts.html' ))
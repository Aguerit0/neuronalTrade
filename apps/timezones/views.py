from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def timezones(request):
    return HttpResponse( render(request, 'timezones/timezones.html' ))

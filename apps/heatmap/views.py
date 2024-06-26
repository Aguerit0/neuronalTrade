from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def heatmap(request):
    return HttpResponse( render(request, 'heatmap/heatmap.html' ))

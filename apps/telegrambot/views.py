from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def telegrambot(request):
    return HttpResponse( render(request, 'telegrambot/telegrambot.html' ))
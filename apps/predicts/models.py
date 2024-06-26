from django.db import models

# Create your models here.

def predicts(request):
    return HttpResponse( render(request, 'predicts/predicts.html' ))
from django.shortcuts import render
import requests
from django.http import JsonResponse

def alerts(request):
    return render(request, 'alerts/alerts.html')

def get_alerts(request):
    # Endpoint FastAPI (corrigiendo el puerto)
    response = requests.get('http://127.0.0.1:5000/alerts/')
    data = response.json()
    return JsonResponse({'alerts': data['alerts']})

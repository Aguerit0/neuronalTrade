from django.urls import path
from apps.alerts import alerts

urlpatterns = [
    path("alerts/", alerts, name="alerts"),
]

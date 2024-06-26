from django.urls import path
from apps.timezones import timezones
urlpatterns = [
    path("timezones/", timezones, name="timezones"),    
]
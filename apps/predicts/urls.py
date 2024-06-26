from django.urls import path
from apps.predicts import predicts

urlpatterns = [
    path("predicts/", predicts, name="predicts"),
]

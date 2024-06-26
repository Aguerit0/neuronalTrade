from django.urls import path
from apps.heatmap import heatmap

urlpatterns = [
    path("heatmap/", heatmap, name="heatmap"),
]
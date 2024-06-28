from django.urls import path
from apps.heatmap import heatmap_view

urlpatterns = [
    path("heatmap/", heatmap_view, name="heatmap"),
]
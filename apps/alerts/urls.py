from django.urls import path, include
from apps.alerts import alerts
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alerts/', views.alerts, name='alerts'),
    path('get_alerts/', views.get_alerts, name='get_alerts'),
]

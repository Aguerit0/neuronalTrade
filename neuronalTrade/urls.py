# neuronalTrade/urls.py

from django.contrib import admin
from django.urls import path
from apps.alerts import views as views_alerts
from neuronalTrade import views as views_base

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views_base.base, name='base'),
        path('alerts/', views_alerts.alerts, name='alerts'),
    
]

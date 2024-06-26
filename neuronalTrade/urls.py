# neuronalTrade/urls.py

from django.contrib import admin
from django.urls import path
from neuronalTrade import views as views_base
from apps.alerts import views as views_alerts
from apps.predicts import views as views_predicts


urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views_base.base, name='base'),
        path('alerts/', views_alerts.alerts, name='alerts'),
        path('predicts/', views_predicts.predicts, name='predicts'),
        
    
]

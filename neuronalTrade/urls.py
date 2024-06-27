# neuronalTrade/urls.py

from django.contrib import admin
from django.urls import path
from neuronalTrade import views as views_base
from apps.alerts import views as views_alerts
from apps.predicts import views as views_predicts
from apps.heatmap import views as views_heatmap
from apps.telegrambot import views as views_telegrambot
from apps.timezones import views as views_timezones

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views_alerts.alerts, name='base'),
        path('alerts/', views_alerts.alerts, name='alerts'),
        path('get_alerts/', views_alerts.get_alerts, name='get_alerts'),
        path('predicts/', views_predicts.predicts, name='predicts'),
        path('heatmap/', views_heatmap.heatmap, name='heatmap'),
        path('telegrambot/', views_telegrambot.telegrambot, name='telegrambot'),
        path('timezones/', views_timezones.timezones, name='timezones'),        
]

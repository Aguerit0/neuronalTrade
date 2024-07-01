# neuronalTrade/urls.py

from django.contrib import admin
from django.urls import path
from neuronalTrade import views as views_base
from apps.alerts import views as views_alerts
from apps.predicts import views as views_predicts
from apps.heatmap import views as heatmap_view
from apps.telegrambot import views as views_telegrambot
from apps.timezones import views as views_timezones
from apps.accounts import views as views_accounts

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views_alerts.alerts, name='base'),
        path('alerts/', views_alerts.alerts, name='alerts'),
        path('get_alerts/', views_alerts.get_alerts, name='get_alerts'),
        path('predicts/', views_predicts.predicts, name='predicts'),
        path('heatmap/', heatmap_view.heatmap_view, name='heatmap'),
        path('telegrambot/', views_telegrambot.telegrambot, name='telegrambot'),
        path('timezones/', views_timezones.timezones, name='timezones'),
        path('signin/', views_accounts.signin, name='signin'),
        path('signup/', views_accounts.signup, name='signup'),
        path('signout/', views_accounts.signout, name='signout'),
]
     
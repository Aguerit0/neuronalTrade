from django.urls import path
from apps.telegrambot import telegrambot
urlpatterns = [
    path("telegrambot/", telegrambot, name="telegrambot"),
]
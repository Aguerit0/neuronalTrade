# apps/alerts/models.py
from django.db import models

class Alerts(models.Model):
    time_interval = models.CharField(max_length=10)
    indicator = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.time_interval} - {self.indicator} - {self.alert}"

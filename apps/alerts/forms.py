# apps/alerts/forms.py
from django import forms
from .models import Alerts

class AlertsForm(forms.ModelForm):
    class Meta:
        model = Alerts
        fields = ['time_interval', 'indicator']

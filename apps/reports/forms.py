from django import forms
from .models import Report


class ReportsForm(forms.ModelForm):
    model = Report
    fields = '__all__'

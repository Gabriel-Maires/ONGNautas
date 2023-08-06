from django import forms
from reports.models import Report

class ReportsForm(forms.ModelForm):
    model=Report
    fields='__all__'
from django import forms
from .models import VoluntaryProjects


class VoluntaryProjectsForm(forms.ModelForm):
    model = VoluntaryProjects
    fields = '__all__'
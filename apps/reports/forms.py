from django import forms
from .models import Report

import re


class ReportsForm(forms.ModelForm):
    
    class Meta:
        model = Report
        fields = [
            'title', 'description', 'cep', 'address', 'complement', 'evidence_image'
        ]

    cep = forms.CharField(max_length=9)
    address = forms.CharField(max_length=64)

    def clean_cep(self) -> str:

        return self._remove_characters('cep')
    
    def clean(self):

        cleaned_data = super().clean()
        cleaned_data['cep'] = self.clean_cep()

        return cleaned_data
    
    def save(self, commit=True):
        
        instance = super().save(commit=False)
        instance.cpf = self.cleaned_data.get('cep')

        if commit:
            instance.save()

        return instance
        
    def _remove_characters(self, key: str) -> str:

        return re.sub(r'[^0-9]', '', self.data[key])

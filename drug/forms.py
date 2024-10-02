from django import forms
from .models import DrugInventory

class DrugInventoryForm(forms.ModelForm):
    class Meta:
        model = DrugInventory
        fields = ['drug_name', 'quantity', 'supplier']
        widgets = {
            'drug_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter drug name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter supplier name'}),
        }
        
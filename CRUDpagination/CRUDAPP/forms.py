from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
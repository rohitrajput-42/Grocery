from django import forms 
from django.forms import ModelForm
from .models import Product

class AddItemForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'quantity', 'unit', 'status')
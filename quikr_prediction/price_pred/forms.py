# forms.py
from django import forms

class CarPriceForm(forms.Form):
    company = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    fuel = forms.CharField(max_length=50)
    kms = forms.IntegerField()

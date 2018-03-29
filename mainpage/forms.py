from django import forms
from .models import *

class ProdutcForm(forms.ModelForm):
    class Meta:
        model = Product
        labels = {
            "expirationDate" : "Expiration Date"
        }
        exclude = [""]

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        exclude = ["products"]
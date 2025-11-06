from django import forms
from products.models import CartItem

class ProductQuantityForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('quantity',)
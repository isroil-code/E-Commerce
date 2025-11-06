from django import forms
from .models import Category, Product, Comment

class SearchForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Sort by Category',
        empty_label='All'
    
    )
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
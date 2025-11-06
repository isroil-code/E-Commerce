from django import forms
from .models import Category, Product, Comment

class SearchForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {'name':'Sort by Category'}
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
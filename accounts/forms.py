from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile, Address

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','phone')
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('country','region','city','address')
        

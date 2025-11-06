from rest_framework import serializers
from accounts.models import UserProfile, Address
from django.contrib.auth.models import User

class AddressSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id','country','region','city','address','created_at')
    
class UserProfileserializer(serializers.ModelSerializer):
    address = AddressSerailizer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'image','phone','created_at', 'address')
    
class Userseriaizer(serializers.ModelSerializer):
    profile = UserProfileserializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile')
        
    
        
        
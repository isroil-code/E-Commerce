from django.shortcuts import render, redirect
from .forms import UserForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile, Address
from .forms import ProfileForm, AddressForm

class RegisterView(View):
    def get(self,req):
        form = UserForm()
        return render(req, 'accounts/register.html', {'form':form})
    def post(self, req):
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(req, 'accounts/register.html', {'form':form})

    
class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    def get(self,req):
        return render(req, 'accounts/login.html')
    def post(self, req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('home')
        return render(req, 'accounts/login.html')
    
class LogoutView(LoginRequiredMixin,View):
  
    def get(self, req):
        logout(req)
        return redirect('index')
        
    
class Profile(LoginRequiredMixin,View):
    def get(self, req):
        profile = UserProfile.objects.get(user=req.user)
        return render(req, 'accounts/profile.html', {'profile':profile})
    
class EditProfile(LoginRequiredMixin, View):
    def get(self, req):
        profile = UserProfile.objects.get(user=req.user)
        address = Address.objects.get(profile=profile)
        if profile or address:
            
            profileform = ProfileForm(instance=profile)
            addressform = AddressForm(instance=address)
            return render(req, 'accounts/edit_profile.html', {
                                                              'profileform':profileform,
                                                              'addressform':addressform})
        return render(req, 'accounts/edit_profile.html', {'error':'Nimadir xato ketdi!'})
        
        
    def post(self, req):
        profile_i = UserProfile.objects.get(user=req.user)
        address_i = Address.objects.get(profile=profile_i)
        profileform = ProfileForm(req.POST, req.FILES, instance=profile_i)
        addressform = AddressForm(req.POST, instance=address_i)
        if profileform.is_valid() and addressform.is_valid():
            profile = profileform.save(commit=False)
            address = addressform.save(commit=False)
            profile.user = req.user
            address.profile = profile
            profile.save()
            address.save()
            return redirect('home')
        return render(req, 'accounts/edit_profile.html', {
                                                              'profileform':profileform,
                                                              'addressform':addressform})
        
        
        
        
        
        
        

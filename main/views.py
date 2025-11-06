from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from serializers.serializers import Userseriaizer
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from products.models import *
from cart.models import Cart
from products.forms import SearchForm
from cart.forms import ProductQuantityForm

#  ===---- serializers ----===  
class get_all(ListAPIView):
    serializer_class = Userseriaizer
    queryset = User.objects.all()
    
class IndexView(View):
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'main/index.html')
    
    
class HomeView(LoginRequiredMixin,View):
    def get(self, req):
        model = Product.objects.all()
        category = SearchForm()
        return render(req, 'main/home.html',{'products':model, 'search':category})
    
    def post(self, req):
        category = SearchForm(req.POST)
        model = Product.objects.filter(category=category)
        return model
    
class ProductDetailView(LoginRequiredMixin,View):
    def get(self, req, pk):
        item = get_object_or_404(Product, pk=pk)
        comments = Comment.objects.filter(product=item)
        return render(req, 'products/detail.html', {'item':item, 'comments':comments})
        
class UserProducts(LoginRequiredMixin, View):
    def get(self, req):
        cart = Cart.objects.get(user=req.user)
        form = None
        try:
            product = Cart.objects.get(user=req.user)
            cartItem = CartItem.objects.get(cart=cart)
            form = ProductQuantityForm(instance=cartItem)
            
        except:
            product = "Savatcha mavjud emas!!!"
        return render(req, 'products/user_products.html', {'product':product, 'form':form})
    def post(self, req):
        cart = Cart.objects.get(user=req.user)
        cartItem = CartItem.objects.get(cart=cart)
        form = ProductQuantityForm(req.POST,instance=cartItem)
        if form.is_valid():
            form.save()
            return redirect('user-products')    
        


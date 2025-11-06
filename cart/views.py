from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from products.models import Product
from .models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import CartItem
from .forms import ProductQuantityForm

class AddToCart(LoginRequiredMixin,View):
    def get(self, req, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(req, 'cart/add_cart.html', {'product':product})
    def post(self, req, pk):
        product = get_object_or_404(Product, pk=pk)
        cart = Cart.objects.get(user=req.user)
        if cart:
            cart.items.create(product=product)
            cart.save()
            return redirect('home')
        
class DeleteProductView(LoginRequiredMixin, View):
    def get(self, req, pk):
        cart = Cart.objects.get(user=req.user)
        product = get_object_or_404(cart.items, pk=pk)
        product.delete()
        return redirect('home')

class UpdateQuantityView(LoginRequiredMixin, View):
    def get(self,req):
        cart = CartItem.objects.get(user=req.user)
        form = ProductQuantityForm(instance=cart)
        return render(req, 'cart/updatequantity.html')
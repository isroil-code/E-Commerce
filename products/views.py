from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm

class ProductListView(ListView):
    template_name = 'products/list.html'
    model = Product.objects.all()
    context_object_name = 'products'

class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    model = Product.objects.all()
    context_object_name = 'p'
    
class ReviewView(LoginRequiredMixin,View):
    def get(self, req, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ReviewForm()
        
        return render(req, 'products/review.html', {'form':form, 'product':product})
    
    def post(self, req, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ReviewForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = req.user
            comment.product = product
            comment.save()
            return redirect('home')
        return render(req, 'products/review.html', {'form':form, 'product':product})
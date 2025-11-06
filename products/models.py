from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('health', 'Health'),
        ('edu', 'Education'),
        ('sports', 'Sports'),
        ('ent', 'Entertainment'),
        ('science', 'Science'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('fashion', 'Fashion'),
        ('business', 'Business'),
    ]
    
    name = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='product')
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def stars(self):
        star = '⭐'
        star_5 = '🌟'
        stars = ''
        if int(self.rate) >= 5:
                stars = star_5 * int(self.rate)
                return stars
        else:
            stars = star * int(self.rate)
            return stars
            
                
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    
    def __str__(self):
        return self.product.name
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.cart.user.username
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from cart.views import AddToCart, DeleteProductView
from products.views import ReviewView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('api/users/', views.get_all.as_view(), name='api'),
    path('user-products/', views.UserProducts.as_view(), name='user-products'),
    path('products/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/<int:pk>/', AddToCart.as_view(), name='addtocart'),
    path('review/product/<int:pk>/', ReviewView.as_view(), name='review'),
    path('delete-product-from-cart/item/<int:pk>/', DeleteProductView.as_view(), name='product_delete')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
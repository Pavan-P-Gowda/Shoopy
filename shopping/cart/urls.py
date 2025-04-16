from django.urls import path 
from .views import viewCart, addToCart, remFromCart

urlpatterns = [
    path('', viewCart, name = 'view_cart'),
    path('addcart/<int:product_id>', addToCart, name= 'add_to_cart'),
    path('remcart/<int:cart_item_id>', remFromCart, name = 'rem_from_cart'), # that after 'int' we write for function based to get particular id not for class baseed
]
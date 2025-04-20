from django.urls import path 
from .views import viewCart, addToCart, remFromCart, addQuantity, remQuantity

urlpatterns = [
    path('', viewCart, name = 'view_cart'),
    path('addcart/<int:product_id>', addToCart, name= 'add_to_cart'),
    path('remcart/<int:cart_item_id>', remFromCart, name = 'rem_from_cart'),
     # above that after 'int' we write for function based to get particular id not for class baseed
     # The below following url patterns will be requested by the JS function
    path('add/<int:cart_item_id>', addQuantity, name='add_quantity'),
    path('remove/<int:cart_item_id>', remQuantity, name='rem_quantity'),
]
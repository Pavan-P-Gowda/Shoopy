from django.shortcuts import render, redirect
from django.template import loader 
from .models import CartItem
from mainapp.models import Product
# Create your views here.

def viewCart(request):
    CartItems = CartItem.objects.filter(user = request.user) 
    # filter means select * from cartitem where 

    template = 'cart.html'

    context = {
        'items' : CartItems
    }
    return render(request,template,context)

def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)
    # get means select * from product whrer id= product_id,
    # it will referecen to indidvidual object (get)

    cart_item, created_id = CartItem.objects.get_or_create(product =  this_product, user = request.user)
    # getor create will help when cart is not added it will add r when cart is already there it will update automaticaly

    cart_item.quantity +=1
    cart_item.save()

    return redirect('view_cart')
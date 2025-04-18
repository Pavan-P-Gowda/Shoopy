from django.shortcuts import render, redirect
from django.template import loader 
from .models import CartItem
from mainapp.models import Product

from django.contrib.auth.decorators import login_required 
# in above 'decortators' will help not to show something error for user when then reload r 
# without login if they add r buy the things soo we import 'login_requried' and add it above every function

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def viewCart(request):
    CartItems = CartItem.objects.filter(user = request.user) 
    # filter means select * from cartitem where  user = request.user ,
    # this gives reference to collection of the items (filter)

    total_price = sum([float(item.product.price)* item.quantity for item in CartItems]) 
    # this is used for  sum the total items in the my cart 
    template = 'cart.html'

    context = {
        'items' : CartItems,
        'total' : total_price
    }
    return render(request,template,context)

@login_required
def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)
    # get means select * from product whrer id= product_id,
    # it will referecen to indidvidual object (get)

    cart_item, created_id = CartItem.objects.get_or_create(product =  this_product, user = request.user)
    # get_or_create will help when cart is not added it will add r when cart is already there it will update automaticaly

    cart_item.quantity +=1
    cart_item.save()

    return redirect('view_cart')

@login_required
def remFromCart(request, cart_item_id) :
    this_cart_item = CartItem.objects.get(id = cart_item_id)
    this_cart_item.delete() #this line will help to delete the cart_item_object and recode in the cartitem table in dbs

    return redirect('view_cart') # return will help go back to viewcart after succeeful deletion of item

@login_required
def  addQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user= request.user)
    cart_item.quantity += 1
    cart_item.save()
    overall_total= sum(item.get_tottal() for item in CartItem.objects.filter(user=request.user))
    context = {
        'quantity' : cart_item.quantity,
        'total_price' : cart_item.get_total(),
        'over_all_total' : overall_total
    }
    return JsonResponse(context)

@login_required
def remQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem,id = cart_item_id,user= request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
        overall_total= sum(item.get_tottal() for item in CartItem.objects.filter(user=request.user))
        context = {
        'quantity' : cart_item.quantity,
        'total_price' : cart_item.get_total(),
        'over_all_total' : overall_total
        }
        return JsonResponse(context)
    else:
        cart_item.delete()
        overall_total= sum(item.get_tottal() for item in CartItem.objects.filter(user=request.user))
        context = {
        'quantity' : 0,
        'total_price' : 0,
        'over_all_total' : overall_total
        }
        return JsonResponse(context)
        

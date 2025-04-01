from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse
 
from django.views.generic import ListView,DetailView, CreateView, UpdateView ,DeleteView

from .models import Product
# Create your views here.
def homeView(request):
    template = loader.get_template('home.html')
    context = {
        # context data to be pulled from the db
        'products' : Product.objects.all()
        #the above line of the code is equivalent to Select * from product_table; 

    }
    return HttpResponse(template.render(context, request))

class ProductDetails(DetailView):
    model = Product
    template_name = 'product_details.html'

def aboutView(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contactView(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))

# crud operations

#read operations we already exploxed above
#lets explre the other

# c-create

class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = '__all__' # this include all the field in the form
    # this view on successful addition of product , redirects the user to a
    #new page , to set this page 
    success_url ='/' # after succefull it will go it will itself back

# u - upadte

class EditProduct(UpdateView):
    model = Product 
    context_object_name = 'product'
    template_name = "edit_product.html"
    fields = ['img' , 'price' , 'stock'] # it will show the particular coloum
    success_url = '/'

# D - delet 
class DeletProduct(DeleteView):
    model = Product
    template_name = 'delet_product.html'
    success_url = '/'
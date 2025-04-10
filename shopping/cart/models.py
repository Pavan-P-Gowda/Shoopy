from django.db import models

# importing the product modle form mainapp as it is a foring key for cartitems
from mainapp.models import Product

# importing the user model from django.contrib.auth as oit is also a forgine key
from django.contrib.auth.models import User 

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE) # cascade will help to delet when staff remove from the cart

    user = models.ForeignKey(User , on_delete = models.CASCADE) 

    quantity = models.IntegerField(default=0)
    #integer 

    date_added = models.DateTimeField(auto_now_add=True)
    # currnt timestamp

    def __str__(self):
        return f"{self.product.name} added by {self.user.username} at {self.date_added}"

from django.urls import path
from . import views

urlpatterns = [
    # path('<urlpattern>',vie.<viefunction>,name='<path_refercens_name>'), this is for function 
    #path('<urlpattern>,view.<classbasedname>.as_view(),name=<'pathname>) this is for class
    path('', views.homeView, name = 'homepage'),
    path('about',views.aboutView, name='aboutpage'),
    path('contact',views.contactView, name='contactpage'),
    path('product/<int:pk>',views.ProductDetails.as_view(),name = 'product_details'),
    path('products/add',views.AddProduct.as_view(), name = 'add_product')
]
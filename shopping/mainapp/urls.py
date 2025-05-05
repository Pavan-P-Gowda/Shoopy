from django.urls import path
from . import views # ". " will say import from this folder file 
urlpatterns = [
    # path('<urlpattern>',vie.<viefunction>,name='<path_refercens_name>'), this is for function 
    #path('<urlpattern>,view.<classbasedname>.as_view(),name=<'pathname>) this is for class
    path('', views.homeView, name = 'homepage'),
    path('about',views.aboutView, name='aboutpage'),
    path('contact',views.contactView, name='contactpage'),
    path('product/<int:pk>',views.ProductDetails.as_view(),name = 'product_details'),
    path('products/add',views.AddProduct.as_view(), name = 'add_product'),
    path('product/edit/<int:pk>',views.EditProduct.as_view(), name = 'edit_product'),
    path('product/delete/<int:pk>' ,views.DeletProduct.as_view(), name = 'delete_product'),
    path('products/search', views.SearchView, name = 'search' )
]
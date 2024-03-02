from django.urls import path
from products.views import *


urlpatterns=[
    
    path('<slug>/',get_products,name="get_products"),
   
]
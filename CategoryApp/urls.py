from django.urls import path
from .views import BarchaProductAPI, AddProduct

urlpatterns = [
    path('all/', BarchaProductAPI.as_view(), name='product'),  
    path('create_category/', AddProduct.as_view(), name='product_create'),  
]

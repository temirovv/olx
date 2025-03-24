from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import BarchaProductAPI, AddProduct, \
    CreateProductAPIView, FilterProductByCategory, \
        ProductView, ProductModelViewSet

router = SimpleRouter()
router.register('products', ProductModelViewSet, basename='products')
print(router.urls)

urlpatterns = [
    path('all/', BarchaProductAPI.as_view(), name='product'),  
    path('create_product/', AddProduct.as_view(), name='product_create'),  
    path('add-product/', CreateProductAPIView.as_view(), name='add-product'),
    path('filter/', FilterProductByCategory.as_view()),
    path('mahsulotlar/', ProductView.as_view()),
    path('', include(router.urls))
]

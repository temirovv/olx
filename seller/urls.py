from django.urls import path
from .views import SellerAccountAPIView, DocumentAPIView, RegistrationsFormAPIView


urlpatterns = [
    path('seller/', SellerAccountAPIView.as_view()),
    path('documents/', DocumentAPIView.as_view()),
    path('registration-form/', RegistrationsFormAPIView.as_view())
]

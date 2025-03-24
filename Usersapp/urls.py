from .views import BarchaUserAPI, RegisterAPI, AddPhoneAPI , UserAPI
from django.urls import path

urlpatterns = [
  path('users/',BarchaUserAPI.as_view(),name='test uchunn yaratdik'),
  path('user/',UserAPI.as_view(),name='name kritilgan userni oladi'),
  path('register/',RegisterAPI.as_view()),
  path('add_phone/',AddPhoneAPI.as_view()),
]

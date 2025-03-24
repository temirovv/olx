from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import UsersModel


class SerializerAlluser(Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  phone = serializers.CharField()
  created_at = serializers.DateTimeField()
  otp = serializers.CharField()
  email = serializers.EmailField()
  age = serializers.IntegerField()

class RegisterSerializer(Serializer):
  name = serializers.CharField()
  age = serializers.IntegerField()
  email = serializers.EmailField()


class AddPhoneSendOtp(Serializer):
  user_id = serializers.CharField()
  phone = serializers.CharField()
# /categories
# /category-products
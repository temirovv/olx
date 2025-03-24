from rest_framework import serializers
from .models import CategoryModel

class SerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

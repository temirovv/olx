from rest_framework import serializers
from .models import ProductModel
from rest_framework import serializers
from .models import ProductModel, Review

class SerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'



class ProductSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    category = serializers.CharField()


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['title', 'description', 'price', 'category']


# products/1/reviews/1/

class ProductGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'title', 'description', 'price', 'old_price', 'category', 'created_at', 'image']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'comment', 'user', 'rating']

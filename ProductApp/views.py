from django.shortcuts import render
from .models import ProductModel
from rest_framework.views import APIView
from .serializers import SerializerProduct, ProductSerializer, CreateProductSerializer, ProductGenericSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet


class BarchaProductAPI(APIView):
    def get(self, request):

        category = request.query_params.get('category-name')
        if category: 
            queryset = ProductModel.objects.filter(category__icontains=category)
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
                
        barcha = ProductModel.objects.all()
        serializer = SerializerProduct(barcha, many=True)
        return Response(serializer.data)


class AddProduct(APIView):
    serializer_class = ProductSerializer

    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category = request.data.get('category')
        try:
            a = ProductModel.objects.create(title=title, description=description, price=price, category=category)
            return Response({'message': 'success saved product','product_id': a.id}, status=201)
        except Exception as e:
            return Response({'message': 'error saving product',
                             'error': f"{e}"},status=400)



class CreateProductAPIView(APIView):
    def post(self, request):
        deserializer = CreateProductSerializer(data=request.data)
        deserializer.is_valid(raise_exception=True)
        deserializer.save()
        return Response(deserializer.data)



class FilterProductByCategory(APIView):
    def get(self, request):
        category = request.query_params.get('category-name')
        if category: 
            queryset = ProductModel.objects.filter(category__icontains=category)
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)

        return Response('okay')



class ProductView(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductGenericSerializer

class ProductModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options']
    serializer_class = ProductGenericSerializer

    def get_queryset(self):
        return ProductModel.objects.all()

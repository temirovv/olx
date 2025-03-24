from django.shortcuts import render
from .models import CategoryModel
from rest_framework.views import APIView
from .serializers import SerializerProduct, ProductSerializer
from rest_framework.response import Response
from rest_framework import status

class BarchaProductAPI(APIView):
    def get(self, request):
        barcha = CategoryModel.objects.all()
        serializer = SerializerProduct(barcha, many=True)
        return Response(serializer.data)

class AddProduct(APIView):
    serializer_class = ProductSerializer

    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        
        if not title or not description:
            return Response({'message': 'Title va Description majburiy'}, status=400)

        try:
            a = CategoryModel.objects.create(title=title, description=description)
            return Response({'message': 'Success! Product saved', 'product_id': a.id}, status=201)
        except Exception as e:
            return Response({'message': 'Error saving product', 'error': str(e)}, status=400)

from django.shortcuts import render
from rest_framework import status

from .models import UsersModel
from rest_framework.views import APIView
from .serializers import SerializerAlluser, RegisterSerializer, AddPhoneSendOtp
from rest_framework.response import Response


class BarchaUserAPI(APIView):
    def get(self, request):
        barcha = UsersModel.objects.all()
        serializer = SerializerAlluser(barcha, many=True)
        return Response(serializer.data)
    

class UserAPI(APIView):
    def get(self, request):
        name_query = request.GET.get('name')
        if name_query:
            barcha = UsersModel.objects.filter(name__icontains=name_query)
        else:
            barcha = UsersModel.objects.all()
            
        serializer = SerializerAlluser(barcha, many=True)
        return Response(serializer.data)

    def delete(self, request):
        name = request.query_params.get('name')  



        if name:
            users = UsersModel.objects.filter(name__icontains=name)
            if not users.exists():
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            deleted_count, _ = users.delete()
            return Response({'message': f'{deleted_count} user(s) deleted'}, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response({'message': 'User ID or Name required'}, status=status.HTTP_400_BAD_REQUEST)

    


class RegisterAPI(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        name_data = request.data.get('name')
        age = request.data.get('age')
        email = request.data.get('email')
        try:
            a = UsersModel.objects.create(name=name_data, age=age, email=email)
            return Response({'message': 'success saved user','user_id': a.id}, status=201)
        except Exception as e:
            return Response({'message': 'error saving user',
                             'error': f"{e}"},status=400)

import random
class AddPhoneAPI(APIView):
    serializer_class = AddPhoneSendOtp
    def put(self, request):
        phone = request.data.get('phone')
        user_id = request.data.get('user_id')
        otp  = str(random.randint(1000,9999))
        barchasi = UsersModel.objects.all().filter(id=user_id).update(phone=phone,otp=otp)
        return Response({'message': 'success saved user','user_id': user_id,"otp":otp}, status=201)


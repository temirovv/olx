from rest_framework.views import APIView
from rest_framework.response import Response

from .models import RegistrationForm, Document, SellerAccount
from .serializers import RegistrationFormSerializer, DocumentSerializer, SellerAccountSerializer


class SellerAccountAPIView(APIView):
    def get(self, request):
        sellers = SellerAccount.objects.all()
        serialize_qilamiz = SellerAccountSerializer(sellers, many=True)
        return Response(serialize_qilamiz.data)

    def post(self, request):
        deserialize_qilamiz = SellerAccountSerializer(data=request.data)
        deserialize_qilamiz.is_valid(raise_exception=True)
        deserialize_qilamiz.save()
        return Response(deserialize_qilamiz.data)


class DocumentAPIView(APIView):
    def get(self, request):
        sellers = Document.objects.all()
        serialize_qilamiz = DocumentSerializer(sellers, many=True)
        return Response(serialize_qilamiz.data)


class RegistrationsFormAPIView(APIView):
    def get(self, request):
        sellers = RegistrationForm.objects.all()
        serialize_qilamiz = RegistrationFormSerializer(sellers, many=True)
        return Response(serialize_qilamiz.data)

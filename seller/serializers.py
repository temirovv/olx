from rest_framework import serializers
from .models import SellerAccount, RegistrationForm, Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'file', 'registration_form']


class SellerAccountSerializer(serializers.ModelSerializer):
    joined_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = SellerAccount
        fields = ['id', 'name', 'phone_number', 'email', 'language', 'joined_at']


class RegistrationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationForm
        fields = ['id', 'registration_type', 'name_of_legal_entity', 'sitr', 'ifut_code', 'seller_account']



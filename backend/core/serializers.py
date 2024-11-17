from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Auditor


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'user_type', 'supervisor', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class AuditorManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model= Auditor
        fields = ['first_name', 'last_name', 'email', 'phone', 'specializations']
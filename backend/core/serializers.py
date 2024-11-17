from django.contrib.auth.hashers import make_password
from rest_framework import serializers

<<<<<<< HEAD
from .models import User,Company
=======
from .models import User, Auditor
>>>>>>> 739cf20975ca17c2917346b70f193e46ae4a7f58


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'user_type', 'supervisor', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


<<<<<<< HEAD
class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name','email','phone','contract_expiration']
=======
class AuditorManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model= Auditor
        fields = ['first_name', 'last_name', 'email', 'phone', 'specializations']
>>>>>>> 739cf20975ca17c2917346b70f193e46ae4a7f58

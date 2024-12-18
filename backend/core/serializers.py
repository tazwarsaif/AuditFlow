from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Company, Auditor, Audit


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'user_type', 'supervisor', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','email','phone','contract_expiration']


class AuditorManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model= Auditor
        fields = ['id','first_name', 'last_name', 'email', 'phone', 'specializations']
        read_only_fields=['id']

class AuditSerializer(serializers.ModelSerializer):
    company_name= serializers.SerializerMethodField()
    auditor_name = serializers.SerializerMethodField()
    class Meta:
        model = Audit
        fields = ['status','start_time','end_time','company_name','auditor_name']
    def get_company_name(self,obj):
        return obj.company.name
    def get_auditor_name(self,obj):
        return f'{obj.auditor.first_name} {obj.auditor.last_name}'



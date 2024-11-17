from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE = (
        ("ADMIN", "ADMIN"),
        ("AUDITOR", "AUDITOR")
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default="ADMIN")
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

class Auditor(models.Model):
    first_name=models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email=models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    specializations=models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    contract_expiration = models.DateField(auto_now_add=False, blank=True, null=True)
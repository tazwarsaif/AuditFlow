from random import choice, choices

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField


class User(AbstractUser):
    USER_TYPE = (
        ("ADMIN", "ADMIN"),
        ("AUDITOR", "AUDITOR")
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default="ADMIN")
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)


class Auditor(models.Model):
    STATUS = (
        ("ONLINE", "ONLINE"),
        ("ON THE WAY", "ON THE WAY"),
        ("OFFLINE", "OFFLINE")
    )
    first_name=models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email=models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    specializations=models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    status=models.CharField(max_length=20, choices=STATUS, default="OFFLINE")
    current_location=CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    contract_expiration = models.DateField(auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return self.name


class Audit(models.Model):
    STATUS = (
        ('COMPLETED',"COMPLETED"),
        ("PENDING","PENDING")
    )
    status = models.CharField(max_length=20,choices=STATUS,default='PENDING')
    auditor = models.ForeignKey(Auditor,null=True, blank=True, on_delete=models.SET_NULL)
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)
    company = models.ForeignKey(Company,null=True, blank=True, on_delete=models.SET_NULL)


class Payment(models.Model):
    STATUS = (
        ('PAID',"PAID"),
        ("PENDING","PENDING"),
        ("OVERDUE","OVERDUE")
    )
    audit = models.ForeignKey(Audit,null=True, blank=True, on_delete=models.SET_NULL)
    due_date = models.DateTimeField(auto_now_add=False)
    pay_date = models.DateTimeField(auto_now_add=False)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')


class AuditReport(models.Model):
    audit = models.ForeignKey(Audit,null=True, blank=True, on_delete=models.CASCADE)
    report = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)


class PerformanceReport(models.Model):
    auditor = models.ForeignKey(Auditor,null=True, blank=True, on_delete=models.SET_NULL)
    performance_report = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
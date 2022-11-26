from django.db import models
from admin.models import Add_doc, Department

# Create your models here.

class Account(models.Model):
    
    userName = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    type = models.CharField(max_length =100)
    user = models.CharField(max_length = 100)

    

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length = 100)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    dob = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    



class Book_appoinment(models.Model):
    user_id = models.ForeignKey(Register, on_delete = models.CASCADE, null = True)
    gender = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, null = True)
    doctor = models.ForeignKey(Add_doc, on_delete = models.CASCADE)

    
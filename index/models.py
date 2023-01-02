from django.db import models
from admin.models import Add_doc, Department


# Create your models here.



class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    dob = models.CharField(max_length=100)
    

class Account(models.Model):

    userName = models.CharField(max_length=100, unique= True)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Add_doc, on_delete=models.CASCADE, null=True)





class Book_appoinment(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Add_doc, on_delete=models.CASCADE)
    prescription = models.CharField(max_length=1000, null=True)
    medicines = models.CharField(max_length=1000, null=True)
    booking_date = models.DateField(null=True)
    booking_time = models.TimeField(null=True)

from django.db import models

# Create your models here.



class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    dob = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    
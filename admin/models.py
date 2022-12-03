
from django.db import models



# Create your models here.



class add_admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Department(models.Model):
    department = models.CharField(max_length = 100)


class Add_doc(models.Model):
    doctorName = models.CharField(max_length = 100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    desc = models.CharField(max_length = 1000)
    quali = models.CharField(max_length = 100)

    


class Add_manager(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)




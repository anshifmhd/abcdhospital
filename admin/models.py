from enum import unique
from unicodedata import name
# from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.



class Add_doc(models.Model):
    username = models.CharField(max_length = 100, unique=True)
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    deprmt = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 1000)
    quali = models.CharField(max_length = 100)


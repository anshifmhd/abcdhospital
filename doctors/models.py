from django.db import models
import datetime
from index.models import Book_appoinment







class BookingTime(models.Model):
    time = models.CharField(max_length=100, null=True)

class BookTime(models.Model):
    time = models.CharField(max_length=100, null=True)

class Consultation_report(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    report = models.CharField(max_length=150)
    medicine = models.CharField(max_length=100)
    bookingtable  =models.ForeignKey(Book_appoinment, on_delete=models.CASCADE, null=True)












  

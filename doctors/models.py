from django.db import models
import datetime

class BookingTime(models.Model):
    date = models.DateField()
    time = models.TimeField()


class Consultation_report(models.Model):
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    report = models.CharField(max_length=150)
    medicine = models.CharField(max_length=100)

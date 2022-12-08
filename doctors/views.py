from pyexpat import model
from django.shortcuts import render
from doctors.models import BookingTime, Consultation_report
from admin.models import Add_doc
from index.models import Book_appoinment, Department

from decorators import login_required
# from . models import *
# Create your views here.


@login_required
def view_doctors(request):
    obj = Add_doc.objects.all()    
    object = Department.objects.all()   
    return render(request,'view_doctors.html', {'details' : obj, 'departments': object })


def index_doctors(request):
    return render(request, "index_doctors.html")



def doctor(request, idd):
    obj = Add_doc.objects.get(id = idd)
    return render(request, "doctor.html", {'doctors' : obj})



def view_profile(request):
    obj = Add_doc.objects.all()
    return render(request, "view_profile.html", {'doctors' : obj})




def add_bookingTime(request):
    if request.method == "POST":
        date = request.POST['date']
        time = request.POST['time']
        obj = BookingTime(date = date, time = time)
        obj.save()

    return render(request, "add_bookingTime.html")


def view_bookings(request):
    obj = Book_appoinment.objects.all()
    return render(request, "view_bookings.html", {'booking' : obj})





def consultation_report(request):
    return render(request, "consultation_report.html")



def send_consultation_report(request):
    if request.method =="POST":
        date = request.POST['date']
        time = request.POST['time']
        report = request.POST['report']
        medicine = request.POST['medicine']

        obj = Consultation_report(date=date, time=time, report=report, medicine=medicine)
        obj.save()

    return render(request, "send_consultation_report.html")


# def view_userDetails(request):
#     details_obj = Register.objects.all()
#     print(details_obj)
#     return render(request,'user_details.html', {'details': details_obj})
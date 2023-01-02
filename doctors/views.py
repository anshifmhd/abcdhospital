from pyexpat import model
from django.shortcuts import render
from doctors.models import BookTime, Consultation_report
from admin.models import Add_doc
from index.models import Book_appoinment, Department, Register, Account
from django.http import JsonResponse
from datetime import date
from datetime import datetime


from decorators import login_required
# from . models import *
# Create your views here.


@login_required
def view_doctors(request):
    obj = Add_doc.objects.all()
    object = Department.objects.all()
    return render(request, 'view_doctors.html', {'details': obj, 'departments': object})


def index_doctors(request):
    return render(request, "index_doctors.html")


def doctor(request, idd):
    obj = Add_doc.objects.get(id=idd)
    return render(request, "doctor.html", {'doctors': obj})


def view_profile(request):
    if request.method == "POST":
        name = request.POST['names']
        # department = request.POST['department']
        quali = request.POST['quali']
        desc = request.POST['desc']
        object = Account.objects.get(id = request.session['userid'])
        Add_doc.objects.filter(id = object.doctor_id).update(doctorName = name, quali = quali, desc = desc)
        

    ss = request.session['userid']
    obj = Account.objects.get(id=ss)
    return render(request, "view_profile.html", {'data': obj})


def add_bookingTime(request):
    if request.method == "POST":
        time = request.POST['time']
        obj = BookTime(time=time)
        obj.save()

    return render(request, "add_bookingTime.html")


def view_bookings(request):
    currentDate = date.today()
    object = Account.objects.get(id = request.session['userid'])
    obj = Book_appoinment.objects.filter(doctor_id = object.doctor_id, booking_date = currentDate)
    
    return render(request, "view_bookings.html", {'booking': obj})


def consultation_report(request):
    return render(request, "consultation_report.html")


def send_prescription(request, pid):
    object = Book_appoinment.objects.get(id = pid)
    if request.method =="POST":
        currentDate = date.today()
        now_method = datetime.now()
        currentTime = now_method.strftime("%H:%M:%S")
        report = request.POST['prescription']
        medicine = request.POST['medicine']
        idd = request.POST['idd']
        obj = Consultation_report(date=currentDate, time=currentTime, report=report, medicine=medicine, bookingtable = object)
        obj.save()
    
    return render(request, "send_prescription.html", {'datas': object})




def depratment_doctors(request):
    department_id = request.POST['department']
    doctors = Add_doc.objects.filter(department=department_id)
    data = [{'id': dep.id, 'doctorName': dep.doctorName, 'department': dep.department.department,
             'quali': dep.quali, 'desc': dep.desc, 'image': dep.image.url} for dep in doctors]
    return JsonResponse({'data': data})

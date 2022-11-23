from django.shortcuts import render,redirect

from admin.models import Add_doc
from decorators import login_required
from index.models import Register
# from . models import *


# Create your views here.


def ind(request):
    return render(request,'index.html')


def heartcentre(request):
    return render(request,'heart_centre.html')


    
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['Phone']
        dob = request.POST['dob']
        username = request.POST['username']
        password = request.POST['password']

        reg = Register(name = name, email = email, address = address, phone = phone, dob = dob,
        userName = username, password = password)
        reg.save()

    return render(request,'register.html')


        
def login(request):
    if request.method == 'POST':
        usern = request.POST['usernam']
        passw = request.POST['pass']
        try:
            user = Register.objects.get(userName = usern, password = passw)
            request.session['userid'] = user.id
            return redirect('index_cust')
        except:
            return render(request,'login.html',{ 'message' : 'invalid username or password' })
    return render(request,'login.html')
 
@login_required
def logout(request):
    del request.session['userid']
    return redirect('log')





def book_appoinment(request):
    return render(request,'book_appoinment.html')

    
def booking_date(request):
    return render(request,'booking_date.html')


def about(request):
    return render(request,'about.html')


def doctors(request):
    return render(request,'doctors.html')



def cardiology(request):
    return render(request,'cardiology.html')



def enquiry(request):
    return render(request,'enquiry.html')


def anaesthesiology(request):
    return render(request,'anaesthesiology.html')


def BloodBank(request):
    return render(request,'BloodBank.html')


def childCare(request):
    return render(request,'childCare.html')


def critical_Care(request):
    return render(request,'critical_Care.html')



def DentalAndMaxillo(request):
    return render(request,'DentalAndMaxillo.html')



def dermatology(request):
    return render(request,'dermatology.html')



def emergency_medicine(request):
    return render(request,'emergency_medicine.html')



def endocrine(request):
    return render(request,'endocrine.html')




def Ent_audiology(request):
    return render(request,'Ent_audiology.html')



def generalMedicine(request):
    return render(request,'generalMedicine.html')



def generalSurgery(request):
    return render(request,'generalSurgery.html')



def liver_gastro(request):
    return render(request,'liver_gastro.html')



def neuro_science(request):
    return render(request,'neuro_science.html')



def orthopaedic(request):
    return render(request,'orthopaedic.html')



def physicalMedicine_rehabilitation(request):
    return render(request,'physicalMedicine_rehabilitation.html')



def psychiatry(request):
    return render(request,'psychiatry.html')


def pulumology(request):
    return render(request,'pulumology.html')



def radioDiagnosis(request):
    return render(request,'radioDiagnosis.html')



def transfusion_medicine(request):
    return render(request,'transfusion_medicine.html')



def womenCare(request):
    return render(request,'womenCare.html')


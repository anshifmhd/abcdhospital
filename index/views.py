from django.shortcuts import render,redirect

from admin.models import Add_doc
from decorators import login_required
from index.models import Register,Book_appoinment,Account
from admin.models import Department, Add_doc
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
        userName = request.POST['username']
        password = request.POST['password']
        

        reg1 = Register(name = name, email = email, address = address, phone = phone, dob = dob)
        account = Account(userName = userName, password = password, type = "user", user = id)
        reg1.save()
        account.save()


    return render(request,'register.html')


        
def login(request):
    if request.method == 'POST':
        usern = request.POST['username']
        passw = request.POST['password']
        try:
            user = Account.objects.get(userName = usern, password = passw)
            request.session['userid'] = user.id
            if (user.type == "doctor"):
                print('hi')
                return redirect('index_doctors')
            elif (user.type == "user"):
                return redirect ('index')
            elif (user.type == "admin"):
                return redirect('index_admin')
            else :
                return redirect ('manager')
        except:
            return render(request,'login.html',{ 'message' : 'invalid username or password' })
    return render(request,'login.html')

@login_required
def logout(request):
    del request.session['userid']
    return redirect('login')




@login_required
def book_appoinment(request):
    
    if request.method == "POST":
        gender = request.POST['gender']
        age = request.POST['gender']
        department_id = request.POST['department']
        department = Department.objects.get( id = department_id)
        doctorName_id = request.POST['doctorName']
        doctorName = Add_doc.objects.get( id = doctorName_id)

        obj = Book_appoinment(gender = gender, age = age, department = department, doctorName = doctorName)
        obj.save()
        return render(request,'book_appoinment.html', {'departments' : Department.objects.all(), 'doctors' :  Add_doc.objects.all() })
    
    
    return render(request,'book_appoinment.html', {'departments' : Department.objects.all(), 'doctors' : Add_doc.objects.all() })
        

    
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


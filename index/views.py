from django.shortcuts import render,redirect

from admin.models import Add_doc
from decorators import login_required
from index.models import Register,Book_appoinment,Account
from admin.models import Department, Add_doc
from doctors.models import BookTime
from django.http import JsonResponse
# from . models import *





# Create your views here.






def ind(request):
    obj = Add_doc.objects.all()
    doctorObj = []

    for i in range(0,4):
        doctorObj.append(obj[i])
        
    return render(request,'index.html',{'doctors':doctorObj})


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
        reg1.save()
        account = Account(userName = userName, password = password, type = "user", user_id = reg1.id)
       
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
                return redirect('doctors:index_doctors')
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
        request.session['gender']=request.POST['gender']
        request.session['age']=request.POST['age']
        request.session['d_id']=request.POST['department']
        request.session['doc_id']=request.POST['doctorName']

        return redirect('booking_date')    
    
    return render(request,'book_appoinment.html', {'departments' : Department.objects.all(), 'doctors' : Add_doc.objects.all() })
        # obj = Book_appoinment(gender = gender, age = age, department = department, doctor = doctorName,
        # user_id_id = request.session['userid'])

    
def booking_date(request):
    
    if request.method == "POST":
        date = request.POST['date']
        booking_time = request.POST['htime']
        ob = Book_appoinment(booking_date = date, booking_time = booking_time, gender = request.session['gender'], age = request.session['age'], doctor_id = request.session['doc_id'], department_id = request.session['d_id'], user_id_id = request.session['userid'])
        ob.save()
    
    obj = BookTime.objects.all()
    return render(request,'booking_date.html',{'time':obj})



# def checkTime(request):




#     pass
    # date1 = request.POST['date']
    # bookTime = Book_appoinment.objects.values('booking_time').filter(booking_date = date1)
    # # print(bookTime)
    # availableTime = BookTime.objects.all()
    # # avail_list=[ for time in availableTime if time not in bookTime]
    
    # # a_time=[]
    # # for i in availableTime:
    # #     if i not in bookTime:
    # #         a_time.append(i)
    # # a_time=set(availableTime).difference(set(bookTime))

    # print('-------------------------')      
    # print(bookTime)
    # print('-------------------------')
    # print(availableTime)

    # return JsonResponse({'key':"vhgvhgf"})

    # # data = [{'id':} for ]


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



# ajax

def dep_doctors(request):
    departmentValue = request.POST['department']

    doctors = Add_doc.objects.filter(department = departmentValue)
    print(doctors)
    data = [{'id':i.id, 'doctorName':i.doctorName, 'department':i.department.department, 'quali':i.quali, 'desc':i.desc, 'image':i.image.url } for i in doctors]
    return JsonResponse({'data':data})



def bookingDetails(request):
    obj = Book_appoinment.objects.all()
    return render(request,'bookingDetails.html',{'data' : obj})
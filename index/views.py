from django.shortcuts import render,redirect

from admin.models import Add_doc
# from . models import *
from customers import views

# Create your views here.


def ind(request):
    return render(request,'index.html')


def heartcentre(request):
    return render(request,'heart_centre.html')


    
def register(request):
    return render(request,'register.html')


        
def login(request):
    if request.method == 'POST':
        usern = request.POST['usernam']
        passw = request.POST['pass']
        try:
            user = Add_doc.objects.get(username = usern, password = passw)
            request.session['userid'] = user.id
            return redirect('index_cust')
        except:
            return render(request,'login.html',{ 'message' : 'invalid username or password' })
    return render(request,'login.html')


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
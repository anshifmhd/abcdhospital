from django.shortcuts import render
from index.models import Register, Account
from doctors.models import Consultation_report




# Create your views here.


def index_customer(request):
    return render(request,'index_customer.html')


def cust_home(request):
    ss = request.session['userid']
    obj = Account.objects.get(id = ss)
    return render(request,'cust_home.html', {'data' : obj})



def health_details(request):
    obj = Consultation_report.objects.all()
    return render(request,'health_details.html',{'reports': obj})
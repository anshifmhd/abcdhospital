from django.shortcuts import render
from index.models import Register, Account, Book_appoinment
from doctors.models import Consultation_report
from admin.models import Add_doc


# Create your views here.


def index_customer(request):
    return render(request, 'index_customer.html')


def cust_home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        dob = request.POST['dob']
        
        oo = Account.objects.get(id = request.session['userid'])
        aaa = Register.objects.filter(id = oo.user_id)
        print(aaa)
        Register.objects.filter(id = oo.user_id).update(name=name, email=email, phone=phone, address=address, dob=dob)
    


    ss = request.session['userid']
    obj = Account.objects.get(id=ss)
    return render(request, 'cust_home.html', {'data': obj})


def update(request):
    
    return render(request, "cust_home.html")


def health_details(request):
    ss = request.session['userid']
    print(ss)
    book = Book_appoinment.objects.get(user_id_id = request.session['userid'])
    print(book)
    
    obj = Consultation_report.objects.filter(bookingtable_id = book)
    print(obj)

    
    return render(request, 'health_details.html', {'reports': obj})

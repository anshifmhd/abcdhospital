from unicodedata import name
from django.shortcuts import render
from .models import Add_doc, Department, Add_manager
from index.models import Register, Account
# Create your views here.


def index_admin(request):
    return render(request, 'index_admin.html')

def add_department(request):
    if request.method == "POST":
        department = request.POST['department']
        obj = Department(department=department)
        obj.save()
    return render(request, 'add_department.html')



def add_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        obj = Account(userName=username, password=password, type="admin")
        obj.save()

    return render(request, "add_admin.html")


def add_doctors(request):
    # obj = ""
    if request.method == "POST":
        usname = request.POST.get("uname")
        pasword = request.POST.get("pass")
        doctorName = request.POST.get("doctorName")
        department_id = request.POST.get("department")
        department = Department.objects.get( id=department_id)
        desc1 = request.POST['des']
        qual = request.POST['qual']
        image = request.FILES['image']

        obj = Add_doc(doctorName=doctorName , department=department, desc=desc1, quali=qual, image=image)
        obj.save()
        account = Account(userName=usname, password=pasword, type="doctor", doctor_id = obj.id)
        account.save()
    return render(request, 'add_doctors.html', {'departments': Department.objects.all()})


def viewRegister(request):
    obj = Register.objects.all()
    return render(request, "view_register.html", {'users': obj})




def add_manager(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pass']
        name = request.POST['name']
        description = request.POST['des']

        managerObj = Add_manager(name=name, description=description)
        account = Account(username=username, password=password,
                          type="manager", user=id)
    return render(request, "add_manager.html")


def view_account(request):
    obj = Account.objects.all()
    return render(request, 'view_account.html', {'accounts': obj})

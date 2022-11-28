from unicodedata import name
from django.shortcuts import render
from .models  import Add_doc, Department, Add_manager
from index.models import Register,Account
# Create your views here.



def index_admin(request):
    return render(request,'index_admin.html')


def add_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        obj = Account(userName = username, password = password, type = "admin")
        obj.save()

    return render(request, "add_admin.html")


def add_doctors(request):
    if request.method == "POST":
        usname = request.POST['uname']
        pasword = request.POST['pass']
        name1 = request.POST['n']
        department_id = request.POST['department']
        department = Department.objects.get( id = department_id)
        desc1 = request.POST['des']
        qual = request.POST['qual']

        add_d = Add_doc(name = name1, department = department, desc = desc1, quali = qual )
        account = Account( userName = usname, password = pasword, type = "doctor", user = id)
        add_d.save()
        account.save()
    return render(request,'add_doctors.html', {'departments' : Department.objects.all() })


def viewRegister(request):
    obj = Register.objects.all()
    return render(request, "view_register.html", {'users' : obj })




def add_department(request):
    if request.method == "POST":
        department = request.POST['department']
        obj = Department( department = department)
        obj.save()
    return render(request,'add_department.html')



def add_manager(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pass']
        name = request.POST['name']
        description = request.POST['des']

        managerObj = Add_manager(name = name, description = description)
        account = Account(username = username, password = password, type = "manager", user = id)
    return render(request, "add_manager.html")
from unicodedata import name
from django.shortcuts import render
from .models  import Add_doc
from index.models import Register
# Create your views here.



def index_admin(request):
    return render(request,'index_admin.html')



def add_doctors(request):
    if request.method == "POST":
        usname = request.POST['uname']
        pasword = request.POST['pass']
        name1 = request.POST['n']
        dep1 = request.POST['dep']
        desc1 = request.POST['des']
        qual = request.POST['qual']

        add_d = Add_doc( username = usname, password = pasword, name = name1, deprmt = dep1, desc = desc1, quali = qual )
        add_d.save()
    return render(request,'add_doctors.html')


def viewRegister(request):
    obj = Register.objects.all()
    return render(request, "view_register.html", {'users' : obj })
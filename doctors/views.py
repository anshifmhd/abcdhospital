from pyexpat import model
from django.shortcuts import render

from admin.models import Add_doc
from decorators import login_required
# from . models import *
# Create your views here.


@login_required
def view_doc(request):
    obj = Add_doc.objects.all()    
    return render(request,'doctors.html', {'details' : obj })








# def view_userDetails(request):
#     details_obj = Register.objects.all()
#     print(details_obj)
#     return render(request,'user_details.html', {'details': details_obj})
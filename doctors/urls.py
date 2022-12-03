from django.urls import path
from . import views


urlpatterns=[
    # path('/',views.),
    path('viewDoctor/',views.view_doc, name = "viewDoctor"),
    path('index_doctors',views.index_doctors, name = "index_doctors"),
    path('doctor',views.doctor, name = "doctor"),






]
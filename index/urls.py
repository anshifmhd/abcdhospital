from django.urls import path
from . import views


urlpatterns=[

    path('',views.ind, name="index"),
    path('heartcentre/',views.heartcentre, name = "heartcentre"),
    path('register/',views.register, name = "register"),
    path('login',views.login, name= 'log'),
    path('logOut',views.logout, name= 'logOut'),
    path('book_appoinment/',views.book_appoinment, name = "book_appoinment"),
    path('booking_date/',views.booking_date, name = "booking_date"),
    path('about/',views.about, name = "about"),
    path('cardiology/',views.cardiology, name = "cardiology"),

    path('anaesthesiology/',views.anaesthesiology, name = "anaesthesiology"),
    path('BloodBank/',views.BloodBank, name = "BloodBank"),
    path('childCare/',views.childCare, name = "childCare"),
    path('critical_Care/',views.critical_Care, name = "critical_Care"),
    path('DentalAndMaxillo/',views.DentalAndMaxillo, name = "DentalAndMaxillo"),
    path('dermatology/',views.dermatology, name = "dermatology"),
    path('emergency_medicine/',views.emergency_medicine, name = "emergency_medicine"),
    path('endocrine/',views.endocrine, name = "endocrine"),
    path('Ent_audiology/',views.Ent_audiology, name = "Ent_audiology"),
    path('generalMedicine/',views.generalMedicine, name = "generalMedicine"),
    path('generalSurgery/',views.generalSurgery, name = "generalSurgery"),
    path('liver_gastro/',views.liver_gastro, name = "liver_gastro"),
    path('neuro_science/',views.neuro_science, name = "neuro_science"),
    path('orthopaedic/',views.orthopaedic, name = "orthopaedic"),
    path('physicalMedicine_rehabilitation/',views.physicalMedicine_rehabilitation, name = "physicalMedicine_rehabilitation"),
    path('psychiatry/',views.psychiatry, name = "psychiatry"),
    path('pulumology/',views.pulumology, name = "pulumology"),
    path('radioDiagnosis/',views.radioDiagnosis, name = "radioDiagnosis"),
    path('transfusion_medicine/',views.transfusion_medicine, name = "transfusion_medicine"),
    path('womenCare/',views.womenCare, name = "womenCare"),

    











]
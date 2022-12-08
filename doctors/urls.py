from django.urls import path
from . import views

app_name = 'doctors'
urlpatterns=[
    # path('/',views.),
    path('view_doctors/',views.view_doctors, name = "view_doctors"),
    path('index_doctors',views.index_doctors, name = "index_doctors"),
    path('view_profile',views.view_profile, name = "view_profile"),
    path('doctor/<int:idd>',views.doctor, name = "doctor"),
    path('add_bookingTime',views.add_bookingTime, name = "add_bookingTime"),
    path('view_bookings',views.view_bookings, name = "view_bookings"),
    path('consultation_report',views.consultation_report, name = "consultation_report"),
    path('send_consultation_report',views.send_consultation_report, name = "send_consultation_report"),

    
    

    








]
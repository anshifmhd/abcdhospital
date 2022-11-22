from django.urls import path
from . import views


urlpatterns=[

    path('',views.ind),
    path('heartcentre/',views.heartcentre, name = "heartcentre"),
    path('register/',views.register, name = "register"),
    path('login',views.login, name= 'log'),
    path('book_appoinment/',views.book_appoinment, name = "book_appoinment"),
    path('booking_date/',views.booking_date, name = "booking_date"),
    path('about/',views.about, name = "about"),
    path('cardiology/',views.cardiology, name = "cardiology"),
    path('enquiry/',views.enquiry, name = "enquiry"),








]
from django.urls import path
from . import views


urlpatterns=[

    path('',views.ind),
    path('heartcentre/',views.heartcentre),
    path('register/',views.register),
    path('login',views.login, name= 'log'),
    path('book_appoinment/',views.book_appoinment),
    path('booking_date/',views.booking_date),
    path('about/',views.about),
    path('cardiology/',views.cardiology),
    path('enquiry/',views.enquiry),








]
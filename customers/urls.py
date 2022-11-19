from django.urls import path
from . import views


urlpatterns=[
    path('index_customer/',views.index_customer, name = "index_cust"),
    path('cust_home/',views.cust_home),




]
from django.urls import path
from . import views

app_name='customers'
urlpatterns=[
    path('index_customer/',views.index_customer, name = "index_customer"),
    path('cust_home/',views.cust_home, name="cust_home"),
    path('health_details/',views.health_details, name="health_details"),





]
from django.urls import path
from . import views


urlpatterns = [

    path('index_admin/',views.index_admin, name = "index_admin"),
    path('add_doctors/',views.add_doctors ),
    path('viewRegister/',views.viewRegister, name = "viewRegister" ),
    path('add_department/',views.add_department, name = "add_department" ),
    path('add_manager/',views.add_manager, name = "add_manager" ),
    path('add_admin/',views.add_admin, name = "add_admin" ),
    path('view_account/',views.view_account, name = "view_account" ),






]
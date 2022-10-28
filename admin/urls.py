from django.urls import path
from . import views


urlpatterns = [

    path('index_admin/',views.index_admin),
    path('add_doctors/',views.add_doctors),

]
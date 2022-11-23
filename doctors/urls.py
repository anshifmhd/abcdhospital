from django.urls import path
from . import views


urlpatterns=[
    # path('/',views.),
    path('viewDoctor/',views.view_doc, name = "viewDoctor"),




]
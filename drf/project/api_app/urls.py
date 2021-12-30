from django.urls import path
from .views import *

urlpatterns = [
    path('info/<int:pk>',student_details,name = "info" ),
    path('info/',student_,name = "all_info" ),
    path('infod/',student_de,name = "inn" ),


]
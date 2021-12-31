from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.student_create ),
    path('info/<int:pk>',views.student_details,name = "info" ),
    path('update/', views.student_update ),
    path('delete/', views.student_delete ),



]

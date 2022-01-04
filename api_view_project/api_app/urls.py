from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api.as_view()),
    path('studentapi/<int:pk>', views.student_api.as_view()),


]
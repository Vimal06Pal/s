from django.contrib import admin
from django.urls import path,include 
from .import views

from rest_framework.routers import DefaultRouter

#create router object
router = DefaultRouter()

#register studentViewset with Router
router.register("studentapi",views.StudentViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),  
    # path('studentapi/', views.student_api.as_view()),
    # path('studentapi/<int:pk>', views.student_api.as_view()),
]
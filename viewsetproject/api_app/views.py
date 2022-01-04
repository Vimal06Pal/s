from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework import viewsets
# Create your views here.


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)



    def create(self,request):
        serializer = StudentSerializer(data = request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk ):
        id = pk  
        print(id)   
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data inserted'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)         

    def partial_update(self,request,pk = None,format = None):
        id = pk
        stu = Student.objects.get(id =id)
        serializer = StudentSerializer(stu,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data inserted'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(self,request,pk = None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})  
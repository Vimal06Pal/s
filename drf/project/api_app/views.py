from django.shortcuts import render
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Student
from .serializer import Studentserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import requests
import json

# Create your views here.

def student_details(request,pk):
    student = Student.objects.get(id = pk)
    print("student=======",student)
    serializer  = Studentserializers(student)
    print("serializer=======",serializer)
    print("serializer_data=======",serializer.data)


    # json_data = JSONRenderer().render(serializer.data)
    # print("json_data=======",json_data)

    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data)


# query set 
def student_(request):
    studen = Student.objects.all()
    print("student=======",studen)
    serializer  = Studentserializers(studen,many = True)
    # print("serializer=======",serializer)
    # print("serializer_data=======",serializer.data)


    # json_data = JSONRenderer().render(serializer.data)
    # print("json_data=======",json_data)

    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data,safe = False)

import io
from rest_framework.parsers import JSONParser



def student_de(request):
    '''converting json_dat to dic using deserializer'''
    studen = Student.objects.all()
    # print("student=======",studen)
    serializer  = Studentserializers(studen,many = True)
    # print("serializer=======",serializer)
    # print("serializer_data=======",serializer.data)


    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # d = json.loads(json_data)
    # print(type(d[0]))
    stream = io.BytesIO(json_data)
    data_list = JSONParser().parse(stream)
    data = data_list[0]
    serializer = Studentserializers(data=data)
    print(serializer.is_valid())
    # print(serializer.errors)
    print(serializer.validated_data)

    # print(type(data))
    # print("json_data=======",json_data)

    return HttpResponse(json_data,content_type="application/json")


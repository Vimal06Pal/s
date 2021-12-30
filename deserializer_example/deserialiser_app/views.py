from django.shortcuts import render
import io
from .serializer import Studentserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import*
from django.http import HttpResponse,JsonResponse

# Create your views here.

@csrf_exempt
def student_create(request):
    print("++++++++++++++++")
    if request.method == "POST":

        json_data = request.body

        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = Studentserializers(data=pythondata)
        print(type(serializer))
        print(serializer.is_valid())
        

        if serializer.is_valid():
            print("++++++++++++++++========================")

            serializer.save()
            msg = {'msg':'Data Inserted'}
            json_data = JSONRenderer().render(msg)
            print(serializer.errors)

            return HttpResponse(json_data,content_type = 'application/json')


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

@csrf_exempt
def student_update(request):
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu =Student.objects.get(id = id)
        serializer = Studentserializers(stu,data=pythondata,partial=True)

        if serializer.is_valid():
            print("++++++++++++++++========================")

            serializer.save()
            msg = {'msg':'Data updated'}
            json_data = JSONRenderer().render(msg)
            print(serializer.errors)

            return HttpResponse(json_data,content_type = 'application/json')

def delete():
    pass
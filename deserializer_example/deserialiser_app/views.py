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
#converting json_data to stream
        stream = io.BytesIO(json_data)
        #stream to python data
        #JSONParser is responsible of converting JSON to dictionary.
        pythondata = JSONParser().parse(stream)
        # converting python dict simple data to query set
        serializer = Studentserializers(data=pythondata)
        print(type(serializer))
        print(serializer.is_valid())
        

        if serializer.is_valid():
            print("++++++++++++++++========================")

            serializer.save()
            msg = {'msg':'Data Inserted'}
            '''data have to return serializer.data back to client in form of JSON,
              not dictionary. Thats what JSONRenderer does. It convert dict to JSON''' 
            json_data = JSONRenderer().render(msg)
            print(serializer.errors)

            return HttpResponse(json_data,content_type = 'application/json')


def student_details(request,pk):
    student = Student.objects.get(id = pk)
    print("student=======",student)
    serializer  = Studentserializers(student)
    print("serializer=======",serializer)
    print("serializer_data=======",serializer.data)
    '''JsonResponse is an HttpResponse subclass that helps to create a JSON-encoded response.
     Its default Content-Type header is set to application/json. 
     The first parameter, data, should be a dict instance. 
     If the safe parameter is set to False, any object can be passed for serialization; 
     otherwise only dict instances are allowed.'''
    return JsonResponse(serializer.data)

@csrf_exempt
def student_update(request):
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu =Student.objects.get(id = id)
        serializer = Studentserializers(stu,data=pythondata,partial=True)  # partial =true 'replace some part of that instance' 

        if serializer.is_valid():
            print("++++++++++++++++========================")

            serializer.save()
            msg = {'msg':'Data updated'}
            json_data = JSONRenderer().render(msg)
            print(serializer.errors)

            return HttpResponse(json_data,content_type = 'application/json')

@csrf_exempt
def student_delete(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = Student.objects.get(id = id)
        stu.delete()
        msg = {'msg':'Data updated'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type = 'application/json')


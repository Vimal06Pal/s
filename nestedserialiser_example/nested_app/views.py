# from django.db.models import query
from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets
from .models import *

# Create your views here.

# class SingerViewSet(viewsets.ModelViewSet):
#     queryset = Singer.objects.all()
#     serializers_class = SingerSerializer

# class SongViewSet(viewsets.ModelViewSet):
#     queryset = Song.objects.all()
#     serializers_class = SongSerializer



from django.shortcuts import render
import io
# from .serializer import Studentserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# from .models import*
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class SingerViewSet(viewsets.ModelViewSet):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id",None)
        if id is not None:
            singer = Singer.objects.get(id = id)
            print("student=======",singer)
            serializers_class = SingerSerializer(singer,many=True)

            # serializer  = SingerSerializer(singer)
            print("serializer=======",serializers_class)
            print("serializer_data=======",serializers_class.data)
            '''JsonResponse is an HttpResponse subclass that helps to create a JSON-encoded response.
            Its default Content-Type header is set to application/json. 
            The first parameter, data, should be a dict instance. 
            If the safe parameter is set to False, any object can be passed for serialization; 
            otherwise only dict instances are allowed.'''
            return JsonResponse(serializers_class.data)

    def post(self,request,*args,**kwargs):
        json_data = request.body
#converting json_data to stream
        stream = io.BytesIO(json_data)
        #stream to python data
        #JSONParser is responsible of converting JSON to dictionary.
        pythondata = JSONParser().parse(stream)
        # converting python dict simple data to query set

        serializer = SingerSerializer(data=pythondata)
        # serializers_class = SingerSerializer()

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
        else:
            msg = {'msg':'Data not Inserted'}
          
            json_data = JSONRenderer().render(msg)
            print(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')



    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu =Singer.objects.get(id = id)
        serializer = SingerSerializer(stu,data=pythondata,partial=True) 
         # partial =true 'replace some part of that instance' 
        # serializer = Studentserializers(stu,data=pythondata)  # partial =true 'replace some part of that instance' 

        if serializer.is_valid():
            print("++++++++++++++++========================")

            serializer.save()
            msg = {'msg':'Data updated'}
            json_data = JSONRenderer().render(msg)
            print(serializer.errors)

            return HttpResponse(json_data,content_type = 'application/json')


    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = Singer.objects.get(id = id)
        stu.delete()
        msg = {'msg':'Data deleted'}
        # json_data = JSONRenderer().render(msg)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(msg,safe=True)

@method_decorator(csrf_exempt,name="dispatch")
class SongViewSet(viewsets.ModelViewSet):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id",None)
        if id is not None:
            student = Song.objects.get(id = id)
            print("student=======",student)
            serializer  = SongSerializer(student)
            print("serializer=======",serializer)
            print("serializer_data=======",serializer.data)
            '''JsonResponse is an HttpResponse subclass that helps to create a JSON-encoded response.
            Its default Content-Type header is set to application/json. 
            The first parameter, data, should be a dict instance. 
            If the safe parameter is set to False, any object can be passed for serialization; 
            otherwise only dict instances are allowed.'''
            return JsonResponse(serializer.data)

    def post(self,request,*args,**kwargs):
        json_data = request.body
#converting json_data to stream
        stream = io.BytesIO(json_data)
        #stream to python data
        #JSONParser is responsible of converting JSON to dictionary.
        pythondata = JSONParser().parse(stream)
        # converting python dict simple data to query set
        serializer = SongSerializer(data=pythondata)
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
        else:
            msg = {'msg':'Data not Inserted'}
          
            json_data = JSONRenderer().render(msg)
            print(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')



    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu =Song.objects.get(id = id)
        serializer = SongSerializer(stu,data=pythondata,partial=True) 
         # partial =true 'replace some part of that instance' 
        # serializer = Studentserializers(stu,data=pythondata)  # partial =true 'replace some part of that instance' 

        if serializer.is_valid():
            print("++++++++++++++++========================")

            serializer.save()
            msg = {'msg':'Data updated'}
            json_data = JSONRenderer().render(msg)
            print(serializer.errors)

            return HttpResponse(json_data,content_type = 'application/json')


    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = Song.objects.get(id = id)
        stu.delete()
        msg = {'msg':'Data deleted'}
        # json_data = JSONRenderer().render(msg)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(msg,safe=True)







       


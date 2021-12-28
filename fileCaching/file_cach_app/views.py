from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'file_cach_app/index.html')

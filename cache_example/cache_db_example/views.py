from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,"cache_example/index.html")

from django.shortcuts import render,HttpResponse
from rest_framework import generics
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Snippets
from .serializer import SnippetsListSerializer,SnippetsDetailSerializer

# Create your views here.
def index(request):
    return HttpResponse("hello world!")

class SnippetsListView(ListAPIView):
    model = Snippets
    serializer_class = SnippetsListSerializer
    def get_queryset(self):
        return Snippets.objects.all()

class SnippetsDetailView(ListAPIView):
    model = Snippets
    serializer_class = SnippetsDetailSerializer
    queryset = Snippets.objects.all()
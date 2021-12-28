from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(20)
def index(request):
    return render(request,'per_view_app/index.html')
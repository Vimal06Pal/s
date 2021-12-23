from django.shortcuts import render,HttpResponse
from kombu.exceptions import HttpError

from mainapp.tasks import test_func

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse('DONE')

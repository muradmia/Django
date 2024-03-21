from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("this is app page")
def main(request):
    return HttpResponse("Hello This is murad")
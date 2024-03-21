from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse("Hello this is contact page")

def home(request):
    return HttpResponse("This is home page")


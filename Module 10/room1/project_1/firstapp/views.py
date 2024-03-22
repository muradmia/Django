from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def contact(request):
    return render(request, 'firstapp/contact.html')
def home(request):
    return render(request, 'firstapp/app_home.html')

def about(request):
    return render(request, 'firstapp/about.html')
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Hello This is home")
    return render(request, 'home.html')

# def home1(request):
#     return render(request, 'templates/index.html')
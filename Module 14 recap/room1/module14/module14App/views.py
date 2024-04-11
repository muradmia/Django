from django.shortcuts import render,redirect
from . import models
from .forms import Student
# Create your views here.
def app(request):
    user = models.Students.objects.all()
    print(user)
    return render(request, 'app.html',{'user': user})

def form(request):
    if request.method == 'POST':
        form = Student(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = Student()
    return render(request, 'form.html',{'form':form})

def delete(request,roll):
    std = models.Students.objects.get(pk = roll).delete()
    return redirect('home')
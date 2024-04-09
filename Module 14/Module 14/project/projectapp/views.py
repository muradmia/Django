from django.shortcuts import render,redirect
from . import models
from .forms import students
# Create your views here.
def app(request):
    user = models.User.objects.all()
    print(user)
    return render(request,'app.html',{'user':user})

def delete_user(request,roll):
    std = models.User.objects.get(pk = roll).delete()
    return redirect('home')

def hey(request):
    # std = students()
    if request.method == 'POST':
        form = students(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = students()
    return render(request,'hey.html',{'form' : form})
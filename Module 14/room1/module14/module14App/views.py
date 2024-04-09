from django.shortcuts import render
from . forms import LoginForm
from . import models
# Create your views here.
def app(request):
    studnet = models.students.objects.all()
    print(studnet)
    return render(request,'app.html',{'data' : studnet})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # name = form.cleaned_data['name']
    else:
        form = LoginForm()
    return render(request,'login.html',{'form' : form})
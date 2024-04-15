from django.shortcuts import render,redirect
from .forms import Profile_form
# Create your views here.
def addprofile(request):
    if request.method == 'POST':
        prifile_form = Profile_form(request.POST)
        if prifile_form.is_valid():
            prifile_form.save()
            return redirect('home')
    else:
        prifile_form = Profile_form()
    return render(request,'addprofile.html',{'prifile_form':prifile_form})
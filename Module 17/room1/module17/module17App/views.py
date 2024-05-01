from django.shortcuts import render,redirect
from .forms import Register
from django. contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def app(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            messages.success(request,"Account create successfully")
            form.save()
            print(form.cleaned_data)
    else:
        form = Register()
    return render(request,'app.html',{'form':form})

def signup(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            messages.success(request,"Account create successfully")
            form.save()
            print(form.cleaned_data)
    else:
        form = Register()
    return render(request,'signup.html',{'form':form})

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name,password = userpass) # check kortesi user database ache kina
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form' : form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user' : request.user})
    else:
        return redirect('login')

def userlogout(request):
    logout(request)
    return redirect('login')
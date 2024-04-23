from django.shortcuts import render
from .forms import Register
# Create your views here.
def app(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save(commit = False)
    else:
        form = Register()
    return render(request,'app.html',{'form':form})
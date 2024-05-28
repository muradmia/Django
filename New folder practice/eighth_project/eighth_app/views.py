from django.shortcuts import render
from .forms import register
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            messages.success(request, 'Account create successful')
            form.save()
            print(form.cleaned_data)
    else:
        form = register()
    return render(request, 'base.html',{ 'form' : form })
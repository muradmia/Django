from django.shortcuts import render
from .forms import Studdent_form
# Create your views here.
def app(request):
    # form = Studdent_form()
    # print(form)

    if request.method == "POST":
        form = Studdent_form(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = Studdent_form()
    return render(request,'app.html',{'form':form})
from django.shortcuts import render
from . forms import contact
# Create your views here.
def app(request):
    return render(request,'app.html')

def about(request):
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     return render(request,'about.html',{'name':name, 'email':email})
    # else:
    return render(request,'about.html')

def forms(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        print(request.POST)
        return render(request,'forms.html',{'name':name, 'email':email ,'select':select})
    else:
        return render(request,'forms.html')


def django_forms(request):
    form = contact(request.POST)
    if form.is_valid():
        print(form.cleaned_data)

    
    return render(request,'django_form.html',{'form' : form})

from django.shortcuts import render
from . forms import contact,student
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

    if request.method == 'POST':
        form = contact(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./module11App/upload/'+file.name,'wb+') as destination:
                for chunk in file.chunk:
                    destination.write(chunk)
            print(form.cleaned_data)
        return render(request,'django_form.html',{'form' : form})
    else:
        form = contact()
    return render(request,'django_form.html',{'form' : form})


    
def student_a(request):
    if request.method == 'POST':
        form = student(request.POST,request.FILES)
        if form.is_valid:
            print(forms.cleaned_data)
        # return render(request,'django_form.html',{'form' : form})
    else:
        form = student()
    return render(request,'django_form.html',{'form' : form})


from django.shortcuts import render
from . forms import LoginForm
# Create your views here.
def app(request):
    return render(request, 'app.html')

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        print(name)
        email = request.POST.get('email')
        return render(request, 'form.html',{'name':name, 'email':email})
    else:
        return render(request, 'form.html')

def django_forms(request):
    form = LoginForm()
    return render(request, 'django_forms.html', {'form':form})
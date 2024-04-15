from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def addauthor(request):
    if request.method == 'POST':
        author_form = forms.Authorform(request.POST)
        if author_form.is_valid():
            author_form.save()
            print(author_form.cleaned_data)
            return redirect('home')
    else:
        author_form = forms.Authorform()
    return render(request, 'author.html',{'form':author_form})
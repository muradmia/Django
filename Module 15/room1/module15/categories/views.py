from django.shortcuts import render,redirect
from .forms import Category_model
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category = Category_model(request.POST)
        if category.is_valid():
            category.save()
            return redirect('home')
    else:
        category = Category_model()
    return render(request, 'category.html',{'category':category})
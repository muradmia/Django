from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author' : 'Rahim','age' : 15,'val' : 20,'lst' : ['python','is','best'],'course' : [
        {
            'id' : 1,
            'name' : 'Murad',
            'fee' : 5000,
        },{
            'id' : 2,
            'name' : 'Sadia',
            'fee' : 5000,
        },{
           'id' : 3,
            'name' : 'Parcej',
            'fee' : 5000, 
        }
    ]}
    return render(request, 'home.html',d)
from django.shortcuts import render,redirect
from . import models
# Create your views here.
def app(request):
    std = student_model()
    print(std)
    return render(request,'app.html',{'std':std})

def delete(request,roll):
    std = models.students.objects.get(pk = roll).delete()
    # print(std)
    # student = models.students.objects.all()
    # # print(student)
    # return render(request,'app.html',{'student':student})
    return redirect('home')
from django.shortcuts import render,redirect
from .forms import Post_form
from .models import Post
from . import forms
# Create your views here.
def addposts(request):
    if request.method == 'POST':
        addpost = forms.Post_form(request.POST)
        if addpost.is_valid():
            addpost.save()
            return redirect('home')
    else:
        addpost = Post_form()
    return render(request,'addposts.html',{'addpost':addpost})


def editpost(request,id):
    po = Post.objects.get(pk=id)
    addpost = forms.Post_form(instance=po)
    print(po.title)
    if request.method == 'POST':
        addpost = forms.Post_form(request.POST,instance=po)
        if addpost.is_valid():
            addpost.save()
            return redirect('Homes')
    return render(request,'addposts.html',{'addpost':addpost})

def deletes(request,id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect('Homes')
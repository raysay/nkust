from django.shortcuts import render
from . import models
from . import forms

def post(request):
    posts = models.post.objects.all()
    return render(request,'blog/post.html',{'posts':posts})

def post_detail(request,pk):
    post = models.post.objects.get(pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    form = forms.PostForm()
    return render(request,'blog/post_new.html',{'form':form})

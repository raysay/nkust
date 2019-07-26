from django.shortcuts import render
from . import models
def post(request):
    posts = models.post.objects.all()
    return render(request,'blog/post.html',{'posts':posts})

def post_detail(request,pk):
    post = models.post.objects.get(pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

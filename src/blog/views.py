from django.shortcuts import render
from . import models
def post(request):
    posts = models.post.objects.all()
    return render(request,'blog/post.html',{'posts':posts})

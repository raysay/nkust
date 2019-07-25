from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def zxc(request):
    return render(request,'123.html')

def use(request):
    return render(request,'test.html')


def rex(request):
    return render(request,'rex.html')

def info(request):
    return render(request, 'Information.html')

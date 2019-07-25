from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def yen(request):
    return render(request,'yen.html')


def rex(request):
    return render(request,'rex.html')

def info(request):
    return render(request, 'Information.html')

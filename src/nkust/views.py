from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def yen(request):
    return render(request,'yen.html')

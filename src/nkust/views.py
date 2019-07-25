from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def use(request):
    return render(request,'test.html')

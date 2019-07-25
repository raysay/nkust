from django.shortcuts import render

def home(request):
    return render(request,'home.html')

<<<<<<< HEAD
def yen(request):
    return render(request,'yen.html')

=======
def use(request):
    return render(request,'test.html')
>>>>>>> 11f3334c3e76dcc9beeeef42521533b47ff6841e

def rex(request):
    return render(request,'rex.html')

def info(request):
    return render(request, 'Information.html')

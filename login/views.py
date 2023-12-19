from django.shortcuts import render
from . import django_form


# Create your views here.
def loginHome(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email') 
        return render(request, "login_home.html", {'name': name, 'email': email})
    
    else:
        return render(request, "login_home.html")

def loginform(request):
    return render(request, "login_from.html")

def djangoForm(request):
    form = django_form.djangoLoginForm()
    print(request.POST)
    return render(request,"django_form.html",{'form':form})
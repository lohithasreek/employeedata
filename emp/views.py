from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Empl
from .forms import EmployeeForm

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def load_form(request):
    form=EmployeeForm
    return render(request,"index.html",{'form':form})

def add(request):
    form=EmployeeForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    employee=Empl.objects.all
    return render(request,'show.html',{'employee':employee})

def edit(request,id):
    employee=Empl.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee=Empl.objects.get(id=id)
    form=EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')

def delete(request,id):
    employee=Empl.objects.get(id=id)
    employee.delete()
    return redirect('/show')

def search(request):
    given_name=request.POST.get('name')
    employee=Empl.objects.filter(ename__icontains=given_name)

    return render(request,'show.html',{'employee':employee})

def reg(request):    
    if request.method=='POST':
        username=request.POST.get("username")
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password1")
        confrim_password=request.POST.get("password2")
        if password==confrim_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username exist')
                return redirect("reg")
            elif User.objects.filter(email=email).exists():
                    messages.info(request,'email exist')
                    return redirect("reg")
            else:
                query=User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                query.save()
        else:
            messages.info(request,"password dont match")
    return render(request,'registration.html')

def login(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         user=auth.authenticate(username=username,password=password)
         if user is not None:
            auth.login(request,user)
            return redirect('/welcome')
         else:
            messages.info(request,"username password not match")
            return redirect("/")

    return render(request,'login.html')

def logout(request):
   auth.logout(request)
   return redirect('')
    

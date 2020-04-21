from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . import models
def homepage(request):
   return render(request,'index.htm')
def appointment(request):
    print('just submitted')
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        user=models.patient(name=fname+lname,email=email,phone=phone)
        user.save()
        print(fname,lname,phone)
        return render(request,'appointment.htm')
    return render(request,'appointment.htm')

    
def help(request):
    return render(request,'help.htm')



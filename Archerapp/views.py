from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def HomePage(request):
    return render (request, 'home.html')


def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('media')
        else:
            return HttpResponse("Username or Passsword is incorrect")
    return render (request, 'Login.html')

def RegisterPage(request):
    if request.method=='POST':
     uname=request.POST.get('Username')   
     email=request.POST.get('Email address') 
     pass1=request.POST.get('pass1') 
     pass2=request.POST.get('pass2')
     
     if pass1!=pass2:
         return HttpResponse('Your password and conform password are not the Same!!')
     else:
         
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
     print(uname,email,pass1,pass2) 
     
    return render (request, 'Register.html')
@login_required(login_url='login')
def MediaPage(request):
    return render (request, 'SocialPg.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')





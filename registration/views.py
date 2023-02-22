from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'Login.html')

def media(request):
    return render(request,'SocialPg.html')
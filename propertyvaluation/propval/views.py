from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
#from django.views.decorators.csrf import ensure_csrf_cookie

#@ensure_csrf_cookie
@login_required(login_url='login')
def Home(request):
    return render (request,'home.html')

def Signup(request):
    if request.method=='POST':
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        uconfpassword = request.POST.get('confpassword')
        if upassword!=uconfpassword:
           return HttpResponse('Password and confirm password does not match')
        #else:
        my_user = User.objects.create_user(uemail,uemail,upassword)
        my_user.save()
       # return HttpResponse('User has been created')
        return redirect('login')
        print(uemail,upassword,uconfpassword)
    return render (request,'signup.html')

def Signin(request):

     if request.method=='POST':
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        user = authenticate(request, username=uemail,password=upassword)
        
        if user is not None:
           login(request , user)
           return redirect('home')
        else:
            return HttpResponse('user name or password is not correct')   
        
     return render (request,'signin.html')

def Logout(request):
    logout(request)
    return redirect('login')

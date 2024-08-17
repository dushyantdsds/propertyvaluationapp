from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserDetails

@login_required(login_url='login')
def Home(request):
    user_details = UserDetails.objects.filter(user_email=request.user.email).first()
    if not user_details:
        return HttpResponse('User data does not exist')
    
    context = {
        'first_name': user_details.first_name or 'Not present',
        'last_name': user_details.last_name or 'Not present',
        'email': request.user.email,
        'phone': user_details.phone or 'Not present',
        'role': user_details.role or 'Not present'
    }
    
    if user_details.role == 'admin':
        return render(request, 'admin_home.html', context)
    elif user_details.role == 'site_engineer':
        return render(request, 'site_engineer_home.html', context)
    elif user_details.role == 'field_engineer':
        return render(request, 'field_engineer_home.html', context)
    else:
        return HttpResponse('Role not present')

def Signup(request):
    if request.method == 'POST':
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        uconfpassword = request.POST.get('confpassword')
        if upassword != uconfpassword:
            return HttpResponse('Password and confirm password do not match')
        
        if User.objects.filter(email=uemail).exists():
            return HttpResponse('Email already exists')
        
        my_user = User.objects.create_user(uemail, uemail, upassword)
        my_user.save()
        UserDetails.objects.create(user=my_user)
        return redirect('login')
    return render(request, 'signup.html')

def Signin(request):
    if request.method == 'POST':
        uemail = request.POST.get('email')
        upassword = request.POST.get('password')
        user = authenticate(request, username=uemail, password=upassword)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is not correct')
    return render(request, 'signin.html')

def Logout(request):
    logout(request)
    return redirect('login')

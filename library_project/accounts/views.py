from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from django.http import JsonResponse
from home.models import Book, Borrow

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        is_admin = request.POST.get('is_admin') == 'true'

        if password != confirm_password:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match', 'username': username, 'email': email})
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html', {'error': 'Username already taken'})
        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/signup.html', {'error': 'Email already registered'})

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, is_admin=is_admin)
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')

    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def current_user(request):
    if request.user.is_authenticated:
        try:
            is_admin = request.user.profile.is_admin
        except:
            is_admin = False
        return JsonResponse({
            'isLoggedIn': True,
            'isAdmin': is_admin
        })
    return JsonResponse({'isLoggedIn': False})

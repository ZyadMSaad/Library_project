from django.shortcuts import render

def home(request):
    return render(request, 'home/Home.html')

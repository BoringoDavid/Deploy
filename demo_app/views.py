from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'demo_app/home.html')

def about(request):
    return render(request, 'demo_app/about.html')

def contact(request):
    return render(request, 'demo_app/contact.html')


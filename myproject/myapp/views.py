from django.shortcuts import render

def home_view(request):
    return render(request, 'myapp/home.html')

def about_view(request):
    return render(request, 'myapp/about.html')

def services_view(request):
    return render(request, 'myapp/services.html')

def contact_view(request):
    return render(request, 'myapp/contact.html')

from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'AppHome/home.html')

def informacion(request):
    return render(request, 'AppHome/about.html')

def account(request):
    return render(request, 'AppHome/account.html')

def mensajes(request):
    return render(request, 'AppHome/mensajes.html')
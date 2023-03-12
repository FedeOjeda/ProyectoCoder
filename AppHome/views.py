from django.shortcuts import render
from django.views.generic import TemplateView

# Vista de la página de inicio.
def inicio(request):
    return render(request, 'AppHome/home.html')

# Vista de la página de about.
def informacion(request):
    return render(request, 'AppHome/about.html')

# Vista de la página de para acceder a las opciones del perfil/usuario.
def account(request):
    return render(request, 'AppHome/account.html')

# Vista de la página de para acceder a las opciones del perfil/usuario.
def mensaje(request):
    return render(request, 'AppHome/mensaje.html')

# Vista de la página con el error 404.
class Error404(TemplateView):
    template_name = 'AppHome/error404.html'
from django.shortcuts import render

# Vista de la página de inicio.
def inicio(request):
    return render(request, 'AppHome/home.html')

# Vista de la página de about.
def informacion(request):
    return render(request, 'AppHome/about.html')

# Vista de la página de para acceder a las opciones del perfil/usuario.
def account(request):
    return render(request, 'AppHome/account.html')

# Vista de la página de para la página mensajes con el error 404.
def error(request):
    return render(request, 'AppHome/404.html')

def page_not_found_view(request, excepción): 
    return render(request, '404.html', estado=404)
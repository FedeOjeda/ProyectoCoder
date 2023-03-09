from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_confirmado(request):
    return render(request, 'AppLogin/login-confirmado.html')

def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django
            
            usuario = form.cleaned_data.get('username')
            con = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=con)

            if user is not None:
                login(request, user)
                contexto = {'mensaje':f'Bienvenido {usuario} a Games - Blog'}
                return render(request, 'AppLogin/login-confirmado.html', contexto)
            
            else:
                contexto = {'mensaje':'El usuario no existe', 'form': form}
                return render(request, 'AppLogin/login.html', contexto)
        
        else:
            contexto = {'mensaje':'Los datos ingresados no son válidos, vuelva a ingresarlos', 'form': form}
            return render(request, 'AppLogin/login.html', contexto)

    form = AuthenticationForm()
    contexto = {'form': form}
    return render(request, 'AppLogin/login.html', contexto)



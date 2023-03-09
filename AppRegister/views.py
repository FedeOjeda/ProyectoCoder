from django.shortcuts import render

from .forms import MyUserCreationForm

# Vista de la página de para registrarse.
def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
      
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            contexto = {'mensaje': 'Usuario creado satisfactoriamente'}
            return render(request, 'AppHome/account.html', contexto)
    
    else:
        form = MyUserCreationForm()
    contexto = {'form': form}
    return render(request, 'AppRegister/sing-up.html', contexto)
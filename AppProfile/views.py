from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from .models import Perfiles, Avatar
from .forms import UserEditForm, PerfilFormulario, CustomPasswordChangeForm

# Vista de la página de para ver las opciones del perfil.
@login_required
def perfildetalle(request):
    return render(request, 'AppProfile/profile.html')

# Vista de la página para cambiar la contraseña.
@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña se actualizo correctamente')
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'AppProfile/cambiar-contraseña.html', {'form': form})

# Vista de la página de para editar los datos del usuario.
@login_required
def editar_usuario(request):
    usuario = User.objects.get(username=request.user)
    
    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST)
        
        if mi_formulario.is_valid():
           
            informacion = mi_formulario.cleaned_data
            
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
           
            usuario.save()
            
            return redirect('/')
            
    else:
        mi_formulario = UserEditForm(initial={'username': usuario.username,
                                            'email': usuario.email,
                                            'first_name': usuario.first_name,
                                            'last_name': usuario.last_name})
        
    return render(request, 'AppProfile/edit-user.html',{'mi_formulario': mi_formulario, 'usuario': usuario})

# Vista de la página de para crear el perfil.
@login_required
def crear_perfil(request):
    if request.method == 'POST':
        form = PerfilFormulario(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/')
    else:
        form = PerfilFormulario()
    context = {'form': form}
    return render(request, 'AppProfile/create-profile.html', context)

# Vista de la página de para editar el perfil.
@login_required
def editar_perfil(request):
    user_profile = request.user.perfiles
    if request.method == 'POST':
        form = PerfilFormulario(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PerfilFormulario(instance=user_profile)
    context = {'form': form}
    return render(request, 'AppProfile/edit-profile.html', context)

# Vista de la página de para ver el perfil.
@login_required
def ver_perfil(request):
    perfil = Perfiles.objects.get(user=request.user)
    contexto = {'perfil':perfil}
    return render(request, 'AppProfile/view-profile.html', contexto)

# Vista de la página de para agregar el avatar.
class AgregarAvatar(LoginRequiredMixin, CreateView):
   
    model = Avatar
    template_name = 'AppProfile/agregar-avatar.html'
    success_url = reverse_lazy('home')
    fields = '__all__'

# Vista de la página de para cambiar el avatar.
class EditarAvatar(LoginRequiredMixin, UpdateView):
    model = Avatar
    template_name = 'AppProfile/agregar-avatar.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
    
    
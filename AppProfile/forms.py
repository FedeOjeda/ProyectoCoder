from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from .models import *

class UserEditForm(forms.Form):
    
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k: '' for k in fields}
        
class PerfilFormulario(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = ('bio', 'link', 'imagen')
        
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}),
        label='Contraseña Actual',
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
        label='Nueva Contraseña',
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        label='Confirmar Contraseña',
    )

        

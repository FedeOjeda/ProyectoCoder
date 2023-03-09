from django.urls import path

from .views import *

urlpatterns = [
    path('profile/', perfildetalle, name ='profile'),
    path('edit-user/', editar_usuario, name ='edit-user'),
    path('create-profile/',crear_perfil, name ='create-profile'),
    path('edit-profile/',editar_perfil, name ='edit-profile'),
    path('view-profile/', ver_perfil, name ='view-profile'),
    path('cambiar-contraseña/', cambiar_contraseña ,name ='cambiar-contraseña'),
    path('crear-avatar/<pk>', AgregarAvatar.as_view(), name ='crear-avatar'),
    path('editar-avatar/<pk>', EditarAvatar.as_view(), name ='editar-avatar'),
]
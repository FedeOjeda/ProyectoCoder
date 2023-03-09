from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name = 'home'),
    path('about/', informacion, name = 'about'),
    path('account/', account, name = 'account'),
    path('mensajes/', mensajes, name = 'mensajes'),
]
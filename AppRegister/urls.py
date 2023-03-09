from django.urls import path
from .views import *

# Urls de la pagína de registro.
urlpatterns = [
    path('sing-up/', register, name = 'sing-up'),
]
from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *

# Urls de las opciones del login.
urlpatterns = [
    path('login/', login_request, name = 'login'),
    path('logout/', LogoutView.as_view(template_name='AppLogin/logout.html'), name='logout'),
]
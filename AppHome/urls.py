from django.urls import path

from .views import *

# Urls de la página de inicio.
urlpatterns = [
    path('', inicio, name = 'home'),
    path('about/', informacion, name = 'about'),
    path('account/', account, name = 'account'),
    path('error/', error, name = 'error')
]
handler404 = 'AppHome.views.page_not_found_view'
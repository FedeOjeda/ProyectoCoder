from django.urls import path
from .views import *

urlpatterns = [
    path('sing-up/', register, name = 'sing-up'),
]
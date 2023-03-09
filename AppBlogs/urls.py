from django.urls import path

from .views import *

# Urls de las opciones del Blog.
urlpatterns = [
    path('crear-blog/', CrearBlog.as_view(), name ='crear-blog'),
    path('lista/<pk>', ListaBlogs.as_view(), name ='lista'),
    path('ver/<pk>', VerBlog.as_view(), name ='ver'),
    path('editar/<pk>', EditarBlog.as_view(), name ='editar'),
    path('borrar/<pk>', BorrarBlog.as_view(), name ='borrar'),

]
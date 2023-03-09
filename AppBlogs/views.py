from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Blogs


# Create your views here.
class CrearBlog(LoginRequiredMixin, CreateView):
   
    model = Blogs
    template_name = 'AppBlogs/crear-blog.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
    
class ListaBlogs(ListView):
    
    model = Blogs
    template_name = 'AppBlogs/lista-blogs.html'
    
class VerBlog(DetailView):
    model = Blogs
    template_name = 'AppBlogs/ver-blog.html'
    
class EditarBlog(LoginRequiredMixin, UpdateView):
    model = Blogs
    template_name = 'AppBlogs/crear-blog.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
    
class BorrarBlog(LoginRequiredMixin, DeleteView):
    model = Blogs
    template_name = 'AppBlogs/eliminar-blogs.html'
    success_url = reverse_lazy('home')
    
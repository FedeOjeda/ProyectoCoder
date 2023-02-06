from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

# Create your views here.
def curso(request):
    curso = Curso(nombres ='Backend', camada='12345')
    curso.save()
    documentoDeTexto = f'Curso: {curso.nombres}, Camada: {curso.camada}'
    
    return HttpResponse(documentoDeTexto)
    
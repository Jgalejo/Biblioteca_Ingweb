from django.shortcuts import render
from .models import Libro, Autores, Categorias  


def mostrar_registros(request):
    libros = Libro.objects.all()
    autores = Autores.objects.all()
    categorias = Categorias.objects.all()
    return render(request, 'index.html', {
        'libros': libros,
        'autores': autores,
        'categorias': categorias
    })

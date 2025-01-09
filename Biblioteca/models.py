from django.db import models

class Autores(models.Model):  
    nombre = models.CharField(max_length=200)
    pais_origen = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Categorias(models.Model): 
    nombre_categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_categoria

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)  
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)  
    anio_publicacion = models.DateField()
    
    def __str__(self):
        return self.titulo

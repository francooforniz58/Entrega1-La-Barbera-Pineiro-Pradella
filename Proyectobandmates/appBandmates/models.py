from django.db import models
from ssl import Options
class Musico(models.Model):
    nombre= models.CharField('nombre',max_length=30)
    edad = models.IntegerField()
    genero = models.CharField('genero',max_length=30) #genero musical
    email= models.EmailField()
    
    def __str__(self): #ponemos la forma de impresion que nosotros queremos para el admin
        return f"{self.nombre}"

class Banda(models.Model):
    nombre= models.CharField('nombre',max_length=30)
    genero = models.CharField('genero',max_length=30) #genero musical
    integrantes = models.IntegerField()
    email= models.EmailField()
        
    def __str__(self): #ponemos la forma de impresion que nosotros queremos para el admin
        return f"{self.nombre}"

class Manager(models.Model):
    nombre= models.CharField('nombre',max_length=30)
    edad = models.IntegerField()
    numero = models.IntegerField()
    email= models.EmailField()
    def __str__(self): #ponemos la forma de impresion que nosotros queremos para el admin
        return f"{self.nombre}"
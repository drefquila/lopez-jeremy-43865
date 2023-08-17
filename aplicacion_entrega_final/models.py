from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Peliculas(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_de_estreno=models.DateField()
    taquilla=models.DecimalField(max_digits=7, decimal_places=2)
    director=models.CharField(max_length=40)
    elenco=models.CharField(max_length=200)
    duracion=models.DurationField(blank=True,null=True)
    sinopsis=models.TextField()
    genero=models.CharField(max_length=40,blank=True,null=True)
    imagen=models.ImageField(upload_to='imagenespeliculas',blank=True,null=True)

class Series(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_de_estreno=models.DateField()
    productor=models.CharField(max_length=40)
    elenco=models.CharField(max_length=200)
    temporadas=models.IntegerField()
    capitulos=models.IntegerField()
    sinopsis=models.TextField()
    genero=models.CharField(max_length=40,blank=True,null=True)
    imagen=models.ImageField(upload_to='imagenespeliculas',blank=True,null=True)

class Programas(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_de_emision=models.DateField()
    director=models.CharField(max_length=40)
    elenco=models.CharField(max_length=200)
    temporadas=models.IntegerField()
    capitulos=models.IntegerField()
    sinopsis=models.TextField()
    imagen=models.ImageField(upload_to='imagenespeliculas',blank=True,null=True)

class Documentales(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_de_estreno=models.DateField()
    director=models.CharField(max_length=40)
    elenco=models.CharField(max_length=200)
    duracion=models.DurationField(blank=True,null=True)
    sinopsis=models.TextField()
    genero=models.CharField(max_length=40,blank=True,null=True)
    imagen=models.ImageField(upload_to='imagenespeliculas',blank=True,null=True)

class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',blank=True,null=True)

    def __str__(self):
        return f'{self.user} [{self.imagen}]'





    


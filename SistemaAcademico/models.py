from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
    username= models.CharField(max_length=30,primary_key=True)
    password= models.CharField(max_length=30)

class Persona(models.Model):
    cedula=models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)


    def __unicode__(self):
        return self.nombre

class Facultad(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre
class Programa(models.Model):
     facultad=models.ForeignKey(Facultad)
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre

class Estudiante(Persona):
    programa = models.ForeignKey(Programa)
    usuario = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.nombre + " " + self.apellido

class Profesor(Persona):
    profesion=models.CharField(max_length=50)


class Bloque(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre
class Aula(models.Model):
     bloque=models.ForeignKey(Bloque)
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre
class Materia(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)
     creditos=models.IntegerField()

     def __unicode__(self):
        return self.nombre

class Pensum(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)
     creditos=models.IntegerField()
     programa=models.ForeignKey(Programa)
     materias=models.ManyToManyField(Materia)

     def __unicode__(self):
        return self.nombre
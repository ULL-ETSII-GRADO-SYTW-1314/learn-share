from django.db import models
from users.models import User
from django.contrib import admin
# Create your models here.


class Curso(models.Model):
  tipo = models.TextField(max_length = 155)
  descripcion = models.TextField(max_length = 155)
  lenguaje = models.TextField(max_length = 155)
  creado = models.DateTimeField(auto_now_add=True)
  creator = models.ForeignKey(User)

class Leccion(models.Model):
  tipo = models.TextField(max_length = 155)
  descripcion = models.TextField(max_length = 155)
  lenguaje = models.TextField(max_length = 155)
  curso = models.ForeignKey(Curso) 
class Tarea(models.Model):
  body = models.TextField(max_length=155)
  leccion = models.ForeignKey(Leccion)
  usuario = models.ForeignKey(User)
class Correcion(models.Model):
  body = models.TextField(max_length=155)
  tarea = models.ForeignKey(Tarea)
  usuario = models.ForeignKey(User)
  nota = models.IntegerField()

class Realiza(models.Model):
  usuario = models.ForeignKey(User)
  curso = models.ForeignKey(Curso)
  comenzado = models.DateTimeField(auto_now_add=True)
  finalizado = models.DateTimeField() 
  nota = models.IntegerField()


##Admin

class CursoAdmin(admin.ModelAdmin):
  list_display = ["tipo", "creado", "creator"]
  list_filter = ["creator"]



admin.site.register(Curso, CursoAdmin)


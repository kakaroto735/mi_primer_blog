from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fechaCreacion = models.DateTimeField(default=timezone.now)
    fechaPublicacion = models.DateTimeField(blank=True, null=True)

    def publicacion(self):
        self.fechaPublicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fechaNacimiento = models.DateTimeField()

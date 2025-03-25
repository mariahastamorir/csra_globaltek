from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=255)
    permisos = models.ManyToManyField('Permiso', related_name='roles') #relacionde muchos a muchos con permisos

    def __str__(self):
        return self.nombre
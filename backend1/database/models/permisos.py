from django.db import models

# Create your models here.
class Permiso(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
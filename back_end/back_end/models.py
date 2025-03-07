from django.db import models

class usuario(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    numero_documento = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)


    def __str__(self):
        return super().__str__()
    

class tipodocumento(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return super().__str__()
    
class empresa(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    nit = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return super().__str__()
    
class roles(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return super().__str__()
    

class permisosxrol(models.Model):

    id = models.AutoField(primary_key=True)
    id_role = models.ForeignKey(roles)
    campo = models.CharField(max_length=100)

    def __str__(self):
        return super().__str__()
    
class permisos(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return super().__str__()
    
class otp_code(models.Model):

    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    create_at = models.DateTimeField(auto_now_add=True)
    exprires_at = models.DateTimeField()

    def __str__(self):
        return super().__str__()    
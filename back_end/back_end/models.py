from django.db import models

class TipoDocumento(models.Model):

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
    
class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    numero_documento = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=225)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id_tipodocumento = models.ForeignKey(TipoDocumento)
    id_empresa = models.ForeignKey(empresa)


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
    
class activos(models.Model):
     id = models.AutoField(primary_key=True)
     nombre = models
     proceso_area = models
     tipo = models
     descripcion = models
     valor = models
     datos_personales = models
     dueno_activo = models
     custodio = models
     fk_id_estadoxactivo = models

class estadoxactivo(models.Model):
    id = models.AutoField(primary_key=True)
    fk_id_activos = models.ForeignKey
    fk_id_confidencialidad = models.ForeignKey
    fk_id_integridad = models.ForeignKey
    fk_id_disponiblidad = models.ForeignKey
    fk_id_criticidad = models.ForeignKey


class confidencialidad(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models
    valor = models

class integridad(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models
    valor = models

class disponibilidad(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models
    valor = models

class criticidad(models.Model):
    id = models
    estado = models
    valor = models


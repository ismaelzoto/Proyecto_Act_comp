from django.db import models
# Create your models here.


class carrera(models.Model):
    clave_oficial = models.CharField(max_length=15,primary_key=True)
    nombre = models.CharField(max_length=70)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos
    def __str__(self):
        return '{}'.format(self.nombre)


class estado(models.Model):
    id_estado = models.SmallIntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=70)
# aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos
    def __str__(self):
        return '{}'.format(self.nombre_estado)


class municipio(models.Model):
    id_municipio = models.SmallIntegerField(primary_key=True)
    nombre_municipio = models.CharField(max_length=70)
    estado = models.ForeignKey(estado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_municipio)


class localidad(models.Model):
    id_localidad = models.BigIntegerField(primary_key=True)
    nombre_localidad = models.CharField(max_length=50)
    municipio = models.ForeignKey(municipio, null=True, blank=True, on_delete=models.CASCADE)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre_localidad)


class rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    # aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos
    def __str__(self):
        return '{}'.format(self.nombre_rol)


class alumnos(models.Model):
    nocontrol = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telefono = models.BigIntegerField(20)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    calle = models.CharField(max_length=50)
    numero_exterior = models.CharField(max_length=50)
    numero_interior = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    estatus = models.CharField(max_length=1)
    carrera = models.ForeignKey(carrera, null=True, blank=True, on_delete=models.CASCADE)
    localidad = models.ForeignKey(localidad, null=True, blank=True, on_delete=models.CASCADE)
    rol = models.ForeignKey(rol, null=True, blank=True, on_delete=models.CASCADE)






"""
despues se ejecuta el comando para realizar la migración del modelo a la base de datos

 python manage.py makemigrations
 python manage.py migrate

se insertan datos a la base de datos con python manage.py shell

 from apps.crud_alumnos.models import carrera
"""
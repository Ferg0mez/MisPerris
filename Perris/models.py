from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#manejo de usuarios perzonalizados
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    perfil=models.CharField(max_length=20,default="Usuario")

class Mascota(models.Model):
    idmascota=models.AutoField(primary_key=True)
    nomascota=models.CharField(max_length=30,verbose_name="Nombre Mascota") #verbose_name = Un nombre legible para el objeto.
    raza=models.CharField(max_length=20,default="")
    descripcion=models.CharField(max_length=50,default="")
    estado=models.CharField(max_length=20,default="Mascota")
    fotografia = models.ImageField(upload_to='fotos/',default="")
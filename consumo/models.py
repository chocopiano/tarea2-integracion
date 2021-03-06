from django.db import models

class Ingredientes(models.Model):
    idi=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False,unique=False)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Hamburguesa(models.Model):
    ide=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=255,blank=False,null=False,unique=False)
    precio=models.IntegerField(blank=False,null=False)
    descripcion=models.TextField()
    imagen=models.CharField(max_length=100)
    ingredients=models.ManyToManyField(Ingredientes)

    def __str__(self):
        return self.nombre







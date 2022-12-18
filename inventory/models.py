from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    descripcion = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)
    ubicacion = models.CharField(max_length=10)
    precio = models.FloatField(max_length=15)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name
from django.db import models
from ckeditor.fields import RichTextField


class Auto(models.Model):
    marca= models.CharField(max_length=30)
    modelo= models.IntegerField()
    descripcion = RichTextField(null=True)
    fecha_creacion= models.DateField(null=True)
    
    def __str__(self):
        return f"La marca del auto es {self.marca} , modelo {self.modelo} y su fecha de creacion es {self.fecha_creacion}"
    

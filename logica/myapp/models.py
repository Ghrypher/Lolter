from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
#Project.object.filter(name__startswith="") Esto busca en la tabla Project, columna name, todo lo que 
#empieza con lo ingresado dentro de las comillas
#Project.task_set.get(id=4) Esto busca en la tabla Project, culumna id, el/los datos que tengan la id
#4, en nuestro caso, esto se podria cambiar por los datos con una linea especifica, como por ej, supp
class Champ(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200) #aca se guarda el icono del champ


class Counter(models.Model):
    champ_selected = models.ForeignKey(Champ,on_delete=models.CASCADE, related_name="counters")
    champ_counter = models.ForeignKey(Champ,on_delete=models.CASCADE, related_name="champ")
    description = models.TextField()

class Roles(models.Model):
    Rol=models.CharField(max_length=200)

class Champrol(models.Model):
    Champ = models.ForeignKey(Champ,on_delete=models.CASCADE)
    Rol = models.ForeignKey(Roles,on_delete=models.CASCADE)

    
#usando "python manage.py makemigrations ____" realizo la actualizacion de la base de datos de ____ app
#usando "python manage.py migrate ____" aplico dicha actualizacion
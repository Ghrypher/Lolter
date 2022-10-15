
from django.test import TestCase
from models import Champ,Champrol,Roles
import django

# Create your tests here.
gus = []
p=Champrol.objects.filter(Rol_id=5)
for jesse in p:
    ww=Champ.objects.filter(id=jesse.Champ_id)
    #print(ww.values('nombre').get()['nombre'])
    gus.append(ww.values('nombre').get()['nombre'])

print(gus)

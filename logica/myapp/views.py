from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Champ, Champrol, Counter
from .forms import buscar

#aca creo las diferentes vistas o pantallas de mi pagina, que en nuestro caso serian 2, la pagina 
#principal, y la pagina de counter, a la cual se accederia una vez clickeado en un champ, mostrando
#toda la data sobre los counters de ese champ

def index(request):

    #[11:14] Los filtros 
    rolChamp = 0
    nombreChamp = ""
    #filtro_nombre = (request.GET["busqueda"])
    champsPorRol = Champrol.objects.filter(Rol_id = rolChamp).values_list("Champ_id")
    champsPorRolYNombre = list(Champ.objects.filter(nombre__startswith = nombreChamp, id__in = champsPorRol).values_list("nombre"))
    listaNombreChamps = []
    for champ in champsPorRolYNombre:
        listaNombreChamps.append(champ[0])
    print ("="*100)
    print (listaNombreChamps)
    print ("="*100)
    listaChampsConFormato = []
    orden = 0
    fila = 6
    columna = len(listaNombreChamps)//6
    for y in range(columna):
        columnaFormateada = []
        for x in range(fila):
            columnaFormateada.append(listaNombreChamps[orden])
            orden += 1
        listaChampsConFormato.append(columnaFormateada)

    columnaFormateada = []
    for x in range(len(listaNombreChamps) - columna * 6):
        columnaFormateada.append(listaNombreChamps[orden])
        orden += 1
    listaChampsConFormato.append(columnaFormateada)




    return render (request,"index.html",
    {
       "champs":(listaChampsConFormato),
       "buscar":buscar()

    }
    )

def champ(request, champname):
    print (champname)
    #TODO se tendria que filtrar la id de un champ mediante el champname, y, mediante esa id, se podrian
    #filtrar sus counters, esto ultimo todavia no es posible por datos de la base de datos, pero de momento
    #estaria bien que se muestren solo la imagen del champ que se eligio
    id_champ = list(Champ.objects.filter(nombre = champname))
    id_counter = list(Counter.objects.filter(champ_selected_id = id_champ[0]).values_list("champ_counter_id", "description"))
    nombre_counter = []
    for counter in id_counter:
        id_champ_counter = list(Champ.objects.filter(id = counter[0]).values_list("nombre"))
        nombre_counter.append(id_champ_counter[0][0])
    print("=" * 100)
    print (id_champ)
    print(id_counter)
    print(nombre_counter)
    print("=" * 100)
    return render (request,"champ.html", {"champname":champname, "counters":id_counter})
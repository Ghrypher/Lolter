from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Champ, Champrol, Counter, Roles
from .forms import buscar

#aca creo las diferentes vistas o pantallas de mi pagina, que en nuestro caso serian 2, la pagina 
#principal, y la pagina de counter, a la cual se accederia una vez clickeado en un champ, mostrando
#toda la data sobre los counters de ese champ

def index(request):

    #[11:14] Los filtros 
    rolChamp = 0
    try:
        nombreChamp = request.GET['Nombre']
    except:
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



def filter(request,lane):

    #[11:14] Los filtros 
    rolChamp = list(Roles.objects.filter(Rol = lane).values_list("id"))
    try:
        nombreChamp = request.GET['Nombre']
    except:
        nombreChamp = ""
    #filtro_nombre = (request.GET["busqueda"])
    champsPorRol = Champrol.objects.filter(Rol_id = rolChamp[0][0]).values_list("Champ_id")
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
    id_champ = list(Champ.objects.filter(nombre = champname))
    id_rol = list(Champrol.objects.filter(Champ_id = id_champ[0]).values_list("Rol_id"))
    
    id_counter = list(Counter.objects.filter(champ_selected_id = id_champ[0]).values_list("champ_counter_id", "description"))
    lista_counters = []
    lista_roles = []
    x = 0
    for rol in id_rol:
        roles = list(Roles.objects.filter(id = rol[0]).values_list("Rol"))
        lista_roles.append(roles[0])
        x += 3
    print("=" * 100)
    print(lista_roles[0][0])
    print("=" * 100)     
    x -= 3
    for i in range(x):
        id_champ_counter = list(Champ.objects.filter(id = id_counter[i][0]).values_list("nombre"))
        lista_counters.append(id_champ_counter)
        lista_counters[i].append(id_counter[i][1])
    lista_roles.pop()
    print("=" * 100)
    print(champname)
    print(lista_counters[0][0][0])
    print(lista_roles[0][0])
    print("=" * 100) 
    #TODO Ahora se almacena el nombre, el rol, y la descripcion de los champs, y se muestran en la pagina
    #la imagen haciendo uso del nombre, y la descripcion, faltaria que se marque cual es el rol del champ
    #elegido, y a que linea pertenecen sus counters
    return render (request,"champ.html", {"champname":champname, "counters":lista_counters, "roles":lista_roles})
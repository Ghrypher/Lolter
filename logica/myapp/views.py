from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Champ, Champrol, Roles
from .forms import buscar

#aca creo las diferentes vistas o pantallas de mi pagina, que en nuestro caso serian 2, la pagina 
#principal, y la pagina de counter, a la cual se accederia una vez clickeado en un champ, mostrando
#toda la data sobre los counters de ese champ

def index(request):

    #[11:14] Los filtros 
    rolChamp = 5
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
    for y in range(len(listaNombreChamps)//6):
        columnaFormateada = []
        for x in range(6):
            columnaFormateada.append(listaNombreChamps[orden])
            orden += 1
        listaChampsConFormato.append(columnaFormateada)

    # return render_to_response(request,
    #   "index.html",
    #   {'grupos': grupos_filtrados},
    # )
    return render (request,"index.html",
    {
       "champs":(listaChampsConFormato),
       "buscar":buscar()

    }
    )

def champ(request):
    return render (request,"champ.html")
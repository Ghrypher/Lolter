from traceback import print_tb
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Champ, Champrol, Roles
from .forms import buscar

#aca creo las diferentes vistas o pantallas de mi pagina, que en nuestro caso serian 2, la pagina 
#principal, y la pagina de counter, a la cual se accederia una vez clickeado en un champ, mostrando
#toda la data sobre los counters de ese champ
def hello(request):

    #[11:14] Los filtros 
    filtro_rol = 0
    filtro_nombre = (request.GET["busqueda"])
    grupo_champs = Champrol.objects.filter(Rol_id=filtro_rol).values_list("Champ_id")
    grupos_filtrados = list(Champ.objects.filter(nombre__startswith=filtro_nombre, id__in=grupo_champs).values_list("nombre"))
    Verdaderos_filtrados = []
    for i in grupos_filtrados:
        Verdaderos_filtrados.append(i[0])

    # return render_to_response(request,
    #   "index.html",
    #   {'grupos': grupos_filtrados},
    # )
    return render (request,"index.html",
    {
       "champs":(Verdaderos_filtrados),
       "buscar":buscar()

    }
    )

def about(request):
    return HttpResponse("about")
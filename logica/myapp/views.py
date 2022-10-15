from traceback import print_tb
from django.http import HttpResponse
from myapp.models import Champ, Champrol, Roles

#aca creo las diferentes vistas o pantallas de mi pagina, que en nuestro caso serian 2, la pagina 
#principal, y la pagina de counter, a la cual se accederia una vez clickeado en un champ, mostrando
#toda la data sobre los counters de ese champ
def hello(request):

    #[11:14] Los filtros 
    filtro_rol = 0 
    filtro_nombre = "Swainn"
    grupo_champs = Champrol.objects.filter(Rol_id=filtro_rol).values_list("Champ_id")
    grupos_filtrados = Champ.objects.filter(nombre__startswith=filtro_nombre, id__in=grupo_champs).values_list("nombre")


    return HttpResponse(grupos_filtrados)
    

def about(request):
    return HttpResponse("about")
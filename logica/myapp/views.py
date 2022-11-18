from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Champ, Champrol, Counter, Roles
from .forms import buscar
from django.db import connection

#aca creo las diferentes vistas o pantallas de mi pagina, que en nuestro caso serian 2, la pagina 
#principal, y la pagina de counter, a la cual se accederia una vez clickeado en un champ, mostrando
#toda la data sobre los counters de ese champ

def obtenerChamps(champ, rol = None, busqueda = None):
    #champ ejemplo
        #champ[
        #   id (no actualmente)
        #   nombre
        #   [rol1, rol2, rol3]
        #   [[counter1, descripcion1], [counter2, descripcion2], [counter3, descripcion3]]
        #]   
    rows = []
    if champ == "Filtrar":
        if  rol:
            if busqueda:
                with connection.cursor() as cursor:
                    cursor.execute("""  SELECT champ.id, champ.nombre, roles.Rol, counter.counters, counter.descrpipciones FROM myapp_champ as champ
                                        JOIN (SELECT champrol.Champ_id, group_concat(roles.Rol, '@') as Rol FROM myapp_champrol as champrol
                                                    JOIN myapp_roles as roles ON champrol.Rol_id = roles.id
                                                    GROUP BY champrol.Champ_id) as roles ON roles.Champ_id = champ.id
                                        JOIN (SELECT  counter.champ_selected_id, group_concat(champs.nombre , '@') as counters, group_concat(counter.description , '@') as descrpipciones  FROM myapp_counter as counter
                                                    JOIN myapp_champ as champs ON counter.champ_counter_id = champs.id
                                                    GROUP BY counter.champ_selected_id	) as counter ON counter.champ_selected_id = champ.id
                                    WHERE champ.nombre LIKE '""" + busqueda + "%' AND roles.Rol LIKE '%" + rol + "%'")
                    rows = cursor.fetchall()
                
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""  SELECT champ.id, champ.nombre, roles.Rol, counter.counters FROM myapp_champ as champ
                                                JOIN (SELECT champrol.Champ_id, group_concat(roles.Rol, '@') as Rol FROM myapp_champrol as champrol
                                                            JOIN myapp_roles as roles ON champrol.Rol_id = roles.id
                                                            GROUP BY champrol.Champ_id) as roles ON roles.Champ_id = champ.id
                                                JOIN (SELECT  counter.champ_selected_id, group_concat(champs.nombre , '@') as counters FROM myapp_counter as counter
                                                            JOIN myapp_champ as champs ON counter.champ_counter_id = champs.id
                                                            GROUP BY counter.champ_selected_id	) as counter ON counter.champ_selected_id = champ.id
                                            WHERE roles.Rol LIKE '%""" + rol + "%'")
                    rows = cursor.fetchall()

        elif busqueda:
            with connection.cursor() as cursor:
                cursor.execute("""  SELECT champ.id, champ.nombre, roles.Rol, counter.counters, counter.descrpipciones FROM myapp_champ as champ
                                        JOIN (SELECT champrol.Champ_id, group_concat(roles.Rol, '@') as Rol FROM myapp_champrol as champrol
                                                    JOIN myapp_roles as roles ON champrol.Rol_id = roles.id
                                                    GROUP BY champrol.Champ_id) as roles ON roles.Champ_id = champ.id
                                        JOIN (SELECT  counter.champ_selected_id, group_concat(champs.nombre , '@') as counters, group_concat(counter.description , '@') as descrpipciones  FROM myapp_counter as counter
                                                    JOIN myapp_champ as champs ON counter.champ_counter_id = champs.id
                                                    GROUP BY counter.champ_selected_id	) as counter ON counter.champ_selected_id = champ.id
                                    WHERE champ.nombre LIKE '""" + busqueda + "%'")
                rows = cursor.fetchall()

    elif champ == "All":
        with connection.cursor() as cursor:
            cursor.execute("""SELECT champ.id, champ.nombre, roles.Rol, counter.counters FROM myapp_champ as champ
            JOIN (SELECT champrol.Champ_id, group_concat(roles.Rol, '@') as Rol FROM myapp_champrol as champrol
                        JOIN myapp_roles as roles ON champrol.Rol_id = roles.id
                        GROUP BY champrol.Champ_id) as roles ON roles.Champ_id = champ.id
            JOIN (SELECT  counter.champ_selected_id, group_concat(champs.nombre , '@') as counters  FROM myapp_counter as counter 
                        JOIN myapp_champ as champs ON counter.champ_counter_id = champs.id
                        GROUP BY counter.champ_selected_id) as counter ON counter.champ_selected_id = champ.id""")
            rows = cursor.fetchall()

    elif champ != None:
        with connection.cursor() as cursor:
            cursor.execute("""  SELECT champ.id, champ.nombre, roles.Rol, counter.counters, counter.descrpipciones FROM myapp_champ as champ
		                            JOIN (SELECT champrol.Champ_id, group_concat(roles.Rol, '@') as Rol FROM myapp_champrol as champrol
					                            JOIN myapp_roles as roles ON champrol.Rol_id = roles.id
					                            GROUP BY champrol.Champ_id) as roles ON roles.Champ_id = champ.id
                                    JOIN (SELECT  counter.champ_selected_id, group_concat(champs.nombre , '@') as counters, group_concat(counter.description , '@') as descrpipciones  FROM myapp_counter as counter
                                                JOIN myapp_champ as champs ON counter.champ_counter_id = champs.id
                                                GROUP BY counter.champ_selected_id	) as counter ON counter.champ_selected_id = champ.id
                                WHERE champ.nombre = %s""", [champ])
            entry = cursor.fetchone()

            champ = []
            #champ.append(entry[0]) #id

            champ.append(entry[1]) #nombre

            rols = entry[2].split('@') # lista de roles
            rols.pop()        
            champ.append(rols)

            counters = entry[3].split('@') # lista de counters
            descripciones = entry[4].split('@') # lista de descripciones
            
            countersCompletos = []
            for i in range(3):
                tempList = []
                tempList.append(counters[i])
                tempList.append(descripciones[i])

                countersCompletos.append(tempList)

            champ.append(countersCompletos)   

        return champ     
    if champ == 'Filtrar' or champ == 'All':
        listadoChamps = []#[champ1,champ2,champ3]
        
        for entry in rows:
            champ = []
            #champ.append(entry[0]) #id
            champ.append(entry[1]) #nombre
            rols = entry[2].split('@') # lista de roles
            rols.pop()        
            champ.append(rols)
            counters = entry[3].split('@') # lista de counters
            champ.append(counters)
            listadoChamps.append(champ)

        print ("="*100)
        print (listadoChamps)
        print ("="*100)

        return listadoChamps


def index(request):
    try:
        nombreChamp = request.GET['Nombre']
    except:
        nombreChamp = None

    try:
        rol = request.GET['rol']
    except:
        rol = None
    
    if rol:
        if nombreChamp:
            listadoChamps = obtenerChamps('Filtrar', rol, nombreChamp)
        else:
            listadoChamps = obtenerChamps('Filtrar', rol)
    elif nombreChamp:
        listadoChamps = obtenerChamps('Filtrar', None, nombreChamp)
    else:
        listadoChamps = obtenerChamps('All')
    
    return render (request,"index.html",
    {
       "listaChamps":(listadoChamps),
       "buscar":buscar(),
       "rol": request.GET.get("rol", ""),
       "Nombre": request.GET.get("Nombre", "")

    }
    )

def champ(request, champname):

    champInfo = obtenerChamps(champname)

    print("=" * 100)
    print(champInfo[0])     # nombre
    print("-" * 25)
    print(champInfo[1][0])  # linea
    print("-" * 25)
    print(champInfo[2][0][0] + "\n"+ champInfo[2][0][1])     # counter n°1
    print("-" * 25)
    print(champInfo[2][1][0] + "\n"+ champInfo[2][1][1])     # counter n°2
    print("-" * 25)
    print(champInfo[2][2][0] + "\n"+ champInfo[2][2][1])     # counter n°3
    print("=" * 100) 

    return render (request,"champ.html", {"champ": champInfo,})
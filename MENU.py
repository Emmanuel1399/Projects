listaPartidos=[]
def Menu():
    print("MENU")
    print("opcion 1) agregar equipo\n"
          "opcion 2) agregar jugador \n"
          "opcion 3) consulta del equipo \n"
          "opcion 4) consultar jugador de un equipo")
    opcion=int(input("escriba la opcion: "))
    if opcion==1:
        agregarEquipo()
    elif opcion ==2:
        agregarJugador()
    elif opcion==3:
        consultarEquipo()
    elif opcion==4:
        consultarJugador()
    else:
        print("opcion invalida")
        Menu()
def agregarEquipo():
    equipo=input("Nombre del equipo: ")
    x={"Equipo":equipo,"jugadores":[]}
    if listaPartidos==[]:
        listaPartidos.append(x)
        Menu()
    else:
        i=0
        while i<len(listaPartidos):
            if equipo==listaPartidos[i]["Equipo"]:
                print("equipo ya existe")
                Menu()
                break
            i+=1
        listaPartidos.append(x)
def agregarJugador():
    equipo=input("equipo al que pertenece el juagador: ")
    jugador=input("jugador a agregar: ")
    i=0
    boolean=False
    if listaPartidos==[]:
        print("No se encuentra ningun equipo registrado")
        Menu()
    else:

        i = 0
        while i < len(listaPartidos):
            if equipo == listaPartidos[i]["Equipo"]:
                boolean=True
                break
            i+=1
        j = 0
        while j < len(listaPartidos):
            if equipo == listaPartidos[j]["Equipo"]:
                e=0
                while e<len(listaPartidos[j]["jugadores"]):
                    if jugador==listaPartidos[j]["jugadores"][e]:
                        print("jugador ya existe en el equipo")
                        Menu()
                        break
                    e+=1
            j+=1
        q=0
        while q<len(listaPartidos):

            if jugador in listaPartidos[q]["jugadores"]:
                print("jugador ya existe en otro equipo")
                Menu()
                break
            q+=1

        if boolean==True:
            i=0
            while i<len(listaPartidos):
                if equipo == listaPartidos[i]["Equipo"]:
                    listaPartidos[i]["jugadores"].append(jugador)
                    Menu()
                    break
                i+=1
        else:
            print("el equipo no existe")
            Menu()

def consultarJugador():
    equipo=input("escriba el equipo a consultar: ")
    if listaPartidos==[]:
        print("no se ha registrado ningun equipo")
    else:
        i=0
        while i<len(listaPartidos):
            if equipo==listaPartidos[i]["Equipo"]:
                print("Equipo ",equipo)
                j=0
                while j<len(listaPartidos[i]["jugadores"]):
                    print(listaPartidos[i]["jugadores"][j])

                    j+=1
                Menu()
                break
            i+=1

def consultarEquipo():
    if listaPartidos==[]:
        print("no se ha registrado ningun equipo")
        Menu()
    else:
        i=0
        while i<len(listaPartidos):

            print("Equipo: ",listaPartidos[i]["Equipo"])
            i+=1
        Menu()
Menu()
def agregarEstudiante(carnetE,nombreE):
    nuevoEstudiante=Estudiante(carnetE,nombreE)
    listaEstudiantes.append(nuevoEstudiante)
    menu()
def agregarCurso(carnet,nombreCurso,notaCursa):
    for estudiante in listaEstudiantes:
       if estudiante.carnet==carnet:
            estudiante.agregarcurso(nombreCurso,notaCursa)
            return
    print("estudiante no registrado")
    menu()
from Estudiante import *
listaEstudiantes=[]
def calcularpromedio(carnet):
    for estudiante in listaEstudiantes:
        print(estudiante.calcularPonderado())
        return
def obtenerHistorial(carnet):
    for x in listaEstudiantes:
        if x.carnet==carnet:
            historial()
def menu():
    print("MENU\n"
          "1) Agregar estudiante: \n"
          "2) Agregar curso: \n"
          "3) Calcular promedio \n"
          "4) Historial\n"
          "5) Salir")
    opcion=input("ingrese la opcion que desea realizar: ")
    if opcion== "1":
        carnet=input("ingrese el carnet: ")
        nombre = input("ingrese el nombre: ")
        agregarEstudiante(carnet,nombre)
    if opcion=="2":
        carnet=input("ingrese el carnet: ")
        nombreC=input("ingrese el nombre del curso: ")
        notaC=int(input("ingrese la nota del curso: "))
        agregarCurso(carnet,nombreC,notaC)
        menu()
    if opcion=="3":
        carnet =input("ingrese el carnet:")
        print("Ponderado" + str(calcularpromedio(carnet)))
        menu()
    if opcion=="4":
        carnet=input("carnet del estudiante a consultar: ")
        obtenerHistorial(carnet)
menu()

from Curso import *
class Estudiante:
    def __init__(self,carnet,nombre):
        self.carnet=carnet
        self.nombre=nombre
        self.listaCurso=[]
    def agregarcurso(self,nombre,nota):
        nuevoCurso=Curso(nombre,nota)
        self.listaCurso.append(nuevoCurso)
    def calcularPonderado(self):
        acumulado=0
        for curso in self.listaCurso:
            acumulado+=curso.nota
        return acumulado/len(self.listaCurso)
    def historial(self,listaestudiante,estudiante):
        i=0
        while i<len(listaestudiante):
            if estudiante==listaestudiante[i]["estudiante"]:
                e=0
                while e<len(listaestudiante[i]["listacurso"]):
                    curso=listaestudiante[i]["listacurso"][e]["curso"]
                    nota=listaestudiante[i]["listacurso"][e]["nota"]
                    e+=1
                    return curso,":",nota
            i+=1
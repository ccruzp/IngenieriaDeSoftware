#!/usr/bin/python
# -*- coding: utf-8 -*-

# CLEI.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que implementa la Conferencia Latinoamericana de Informática CLEI

from Articulo import *
from ComitePrograma import *
from Persona import *
from Miembro import *
from operator import methodcaller

class CLEI(object):
    
    numComi = 0

    # Constructor
    def __init__(self):
        self.fechaInicio = None
        self.fechaFin = None
        self.topicos = []

        self.comites = {}
        self.personas = []
        self.articulos = []
        self.articulosAceptados = []
        self.articulosEmpatados = []

    def agregarTopico(self, tema):
        self.topicos.append(tema)


    # Crea un nuevo artículo y lo agrega a la lista de artículos del CLEI
    def nuevoArticulo(self, titulo, tema):
        articulo = Articulo(titulo, tema)
        self.articulos.append(articulo)
        

    def listarArticulosAceptados(self):
         for articulo in sorted(self.articulos, reverse = True):
             print articulo.promedioEvaluaciones()
             if articulo.aceptado:
                 print articulo

    def addMiembro(self,numComite,nombre, inst, correo, dirpost,
                   numero, url=None):
        miembro = Miembro(nombre, inst, correo, dirpost, numero, url)
        try:
            self.comites[numComite].addMiembro(miembro)
            return True 
        except KeyError, e:
            return False

    def setPresidente(self,numComite, miembro):
        return self.comites[numComite].setPresi(miembro)

    def addComites(self, topico):
        comite = ComitePrograma()
        comite.topicos.append(topico)
        self.numComi+=1
        self.comites[str(self.numComi)]=comite
    
    def generarListas(self):
        tam = int(raw_input("Introduzca el tamaño máximo que debe tener la lista de aceptados: "))
        if tam > len(self.articulos):
            print "No hay suficientes artículos inscritos"
            return
        self.llenarListas(tam)

    # Genera las listas de artículos aceptados y de artículos empatados.
    def llenarListas(self, tam):
        # Contador
        i = 0 
        # Ordena la lista de acuerdo al promedio de sus calificaciones
        lista = sorted(self.articulos, reverse = True, key = methodcaller('promedioEvaluaciones'))
        # Si el tamaño máximo de la lista de aceptados es igual a la cantidad de artículos inscritos se agregan todos a la lista de aceptados
        if tam == len(lista):
            for articulo in lista:
                self.articulosAceptados.append(articulo)
            return
        # Recorre la lista comparando el promedio de cada elemento con el promedio del primer
        # primer elemento que quedaría fuera
        while i < tam:
            promedio = lista[i].promedioEvaluaciones()
            aceptado = lista[i].verificarAceptacion()
            # Si los valores son iguales lo agrega a la lista de empatados y luego agrega todos los
            # artículos que queden en la lista que tengan el mismo promedio
            if promedio == lista[tam].promedioEvaluaciones() and aceptado:
                while promedio == lista[tam].promedioEvaluaciones():
                    self.articulosEmpatados.append(lista[i])
                    i += 1
                    if i == len(lista):
                        return
                    promedio = lista[i].promedioEvaluaciones()
                return
            # Si el valor es mayor entonces lo agrega a la lista de aceptados
            elif aceptado:
                self.articulosAceptados.append(lista[i])
            i += 1

    def __str__(self):
        articulos = ''
        for c in self.articulos:
            articulos += str(c)
        comites = ''
        for c in self.comites.values():
            comites += '\n'+str(c)
        articulosAceptados = ''
        for c in self.articulosAceptados:
            articulosAceptados += str(c)
        articulosEmpatados = ''
        for c in self.articulosEmpatados:
            articulosEmpatados += str(c)

            
        return 'Comites:\n'+comites+'\n'\
            '\nArticulos:\n'+articulos+'\n'\
            '\nArticulos Aceptados:\n'+articulosAceptados+'\n'\
            '\nArticulos Empatados:\n'+articulosEmpatados

if __name__ == "__main__":
    clei = CLEI()
    clei.nuevoArticulo("Uno", "Prueba")
    clei.articulos[0].calificar(2)
    clei.articulos[0].calificar(4)
    clei.nuevoArticulo("Dos", "Prueba")
    clei.articulos[1].calificar(5)
    clei.articulos[1].calificar(5)
    clei.nuevoArticulo("Tres", "Prueba")
    clei.articulos[2].calificar(2)
    clei.articulos[2].calificar(5)
    clei.nuevoArticulo("Cuatro", "Prueba")
    clei.articulos[3].calificar(4)
    clei.articulos[3].calificar(3)
    clei.generarListas()
    print "A"
    print len(clei.articulosAceptados)
    for a in clei.articulosAceptados:
        print a

    print "B"
    for b in clei.articulosEmpatados:
        print b


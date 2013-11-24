#!/usr/bin/python
# -*- coding: utf-8 -*-

# CLEI.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que implementa la Conferencia Latinoamericana de Informática CLEI

from Articulo import *
from operator import methodcaller

class CLEI(object):

    # Constructor
    def __init__(self):
        self.fechaInicio = None
        self.fechaFin = None
        self.topicos = []
        self.articulos = []
        self.articulosAceptados = []
        self.articulosEmpatados = []

    # Crea un nuevo artículo y lo agrega a la lista de artículos del CLEI
    def nuevoArticulo(self, titulo, tema):
        articulo = Articulo(titulo, tema)
        self.articulos.append(articulo)
        
    # Genera las listas de artículos aceptados y de artículos empatados.
    def generarListas(self):
        # Contador
        i = 0 
        # Recibe el tamaño máximo que debe tener la lista de aceptados.
        tam = int(raw_input("Introduzca el tamaño de la lista de aprobados: "))
        if tam > len(self.articulos):
            print "No hay suficientes artículos inscritos"
            return

        # Ordena la lista de acuerdo al promedio de sus calificaciones
        lista = sorted(self.articulos, reverse = True, key = methodcaller('promedioEvaluaciones'))
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
    for a in clei.articulosAceptados:
        print a

    print "B"
    for b in clei.articulosEmpatados:
        print b

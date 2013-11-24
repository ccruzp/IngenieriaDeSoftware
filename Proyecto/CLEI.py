#!/usr/bin/python
# -*- coding: utf-8 -*-

# CLEI.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que representa la Conferencia Latinoamericana de Informática CLEI

from Articulo import *
from ComitePrograma import *
from Persona import *
from Miembro import *

class CLEI(object):
    
    numComi = 0

    # Constructor
    def __init__(self):
        self.fechaInicio = None
        self.fechaFin = None
        self.topicos = []
        self.listaArticulos = []
        self.comites = {}
        self.personas = []

    def agregarTopico(self, tema):
        self.topicos.append(tema)

    def nuevoArticulo(self, titulo, tema):
        articulo = Articulo(titulo, tema)
        self.listaArticulos.append(articulo)

    def listarArticulosAceptados(self):
         for articulo in sorted(self.listaArticulos, reverse = True):
             print articulo.promedioEvaluaciones()
             if articulo.aceptado:
                 print articulo

    def addMiembro(self,numComite,nombre, inst, correo, dirpost,
                   numero, url=None):
        miembro = Miembro(nombre, inst, correo, dirpost, numero, url)
        self.comites[numComite].addMiembro(miembro)

    def setPresidente(self,numComite, miembro):
        return self.comites[numComite].setPresi(miembro)

    def addComites(self, topico):
        comite = ComitePrograma()
        comite.topicos.append(topico)
        self.numComi+=1
        self.comites[str(self.numComi)]=comite


if __name__=="__main__":

    clei = CLEI()
    clei.nuevoArticulo("Avion", "Probar")
    clei.listaArticulos[0].calificar(2)
    clei.listaArticulos[0].calificar(5)
    
    clei.nuevoArticulo("Zapato", "Otro")
    clei.listaArticulos[1].calificar(5)
    clei.listaArticulos[1].calificar(3)

    print clei.listaArticulos[0]
    print clei.listaArticulos[1]

    clei.listarArticulosAceptados()

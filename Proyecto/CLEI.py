#!/usr/bin/python
# -*- coding: utf-8 -*-

# CLEI.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que representa la Conferencia Latinoamericana de Informática CLEI

from Articulo import *

class CLEI(object):
    
    # Constructor
    def __init__(self):
        self.fechaInicio = None
        self.fechaFin = None
        self.topicos = []
        self.listaArticulos = []

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

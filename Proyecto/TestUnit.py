#!/usr/bin/python
# -*- coding: utf-8 -*-

# TestUnit.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Unidad de pruebas 
# 
# https://wiki.python.org/moin/PyUnit
# http://pyunit.sourceforge.net/pyunit.html

import unittest
from Articulo import *

# Modulo de prueba de la clase Articulo
class PruebaArticulo(unittest.TestCase):

    def setUp(self):
        self.Articulo = Articulo("Articulo de Prueba","Pruebas")
        
#    def tearDown(self):
        
    # prueba del metodo calificar
    def testCalificar(self):

        self.Articulo.calificar(0)
        assert self.Articulo.calificacion == [0], "Falla agregando 1ra nota"

        self.Articulo.calificar(0)
        assert self.Articulo.calificacion == [0,0], "Falla agregando 2da nota"

        # limpia clasificacion al final de la prueba
        self.Articulo.calificacion[:]=[]

    # prueba del metodo promedioEvaluaciones
    def testPromedioEvaluaciones(self):

        # Promedio de 0 y 0 
        self.Articulo.calificar(0)
        self.Articulo.calificar(0)

        assert self.Articulo.promedioEvaluaciones() == 0.0, "Falla con el promedio de 0"
        self.Articulo.calificacion[:]=[]

        # Promedio de varios numeros
        self.Articulo.calificar(2)
        self.Articulo.calificar(3)
        self.Articulo.calificar(4)
        self.Articulo.calificar(5)
        
        assert self.Articulo.promedioEvaluaciones() == 3.5, "Falla con mas de 2 numeros"
        self.Articulo.calificacion[:]=[]

    # prueba del metodo verificar Evaluaciones
    def testVerificarAceptacion(self):
        
        # Numeros cuyo promedio > 3
        self.Articulo.calificar(2)
        self.Articulo.calificar(3)
        self.Articulo.calificar(4)
        self.Articulo.calificar(5)

        assert self.Articulo.verificarAceptacion(), "Falla con promedio mayor a 3"
        self.Articulo.calificacion[:]=[]

        # Numeros cuyo promedio = 3
        self.Articulo.calificar(3)
        self.Articulo.calificar(3)

        assert self.Articulo.verificarAceptacion(), "Falla con promedio igual a 3"
        self.Articulo.calificacion[:]=[]

        # Numeros cuyo promedio < 3
        self.Articulo.calificar(2)
        self.Articulo.calificar(3)
        assert not self.Articulo.verificarAceptacion(), "Falla con promedio menor a 3"
        self.Articulo.calificacion[:]=[]

    # No se si haga falta esto pero lo puse por si acaso 
    def test__str__(self):
        for i in range(1,5):
            self.Articulo.calificar(i)

        assert str(self.Articulo) == self.Articulo.tema+' '+self.Articulo.titulo+': '+str(self.Articulo.calificacion)

# class PruebaCLEI(unittest.testcase):
    
#     def setUp(self):
#         self.CLEI = CLEI()
    
    # def testNuevoArticulo(self):
    #     self.nuevoArticulo(self, "Titulo", "Tema")
    #     assert(self.NuevoArticulo() == [0], "Falló creación")
    #     self.articulos[:] = []
        
    # def testGenerarLista(self):
    #     clei.nuevoArticulo("Uno", "Prueba")
    #     clei.articulos[0].calificar(2)
    #     clei.articulos[0].calificar(4)
    #     clei.nuevoArticulo("Dos", "Prueba")
    #     clei.articulos[1].calificar(5)
    #     clei.articulos[1].calificar(5)
    #     clei.nuevoArticulo("Tres", "Prueba")
    #     clei.articulos[2].calificar(2)
    #     clei.articulos[2].calificar(5)
    #     clei.nuevoArticulo("Cuatro", "Prueba")
    #     clei.articulo[3].calificar(4)
    #     clei.articulo[3].calificar(3)
    #     assert(self.articulosAceptados == [2], "Falló la generación de lista de aceptados")
    #     assert(self.articulosEmpatados == [], "Falló la generación de lista de empatados")

if __name__=="__main__":
    unittest.main()

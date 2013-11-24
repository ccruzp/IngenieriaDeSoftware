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
from ComitePrograma import *
from Miembro import *
from Persona import *
from CLEI import *

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

        # Numeros cuyo promedio = 3 pero menos de 2 personas lo calificaron
        self.Articulo.calificar(3)

        assert self.Articulo.verificarAceptacion(), "Falla con menos de 2 personas"
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

class PruebaComitePrograma(unittest.TestCase):

    def setUp(self):
        self.comite = ComitePrograma()
        
    def testAddMiembro(self):
        miembro1 = Miembro("Jose", "USB", "jusb@hotmail.com" ,"1342", "1234567")
        miembro2 = Miembro("Pedro", "BSU", "pusb@hotmail.com" ,"1432", "1243567")

        self.comite.addMiembro(miembro1)
        assert self.comite.miembros == [miembro1], "No esta agregando a miembro 1"

        self.comite.addMiembro(miembro2)
        assert self.comite.miembros == [miembro1,miembro2],\
            "No esta agregando a miembro 2"

    def testSetPresi(self):
        presi = Miembro("Manic","BUS","mic@mand.te","8888","88888")
        miembro1 = Miembro("Jose", "USB", "jusb@hotmail.com" ,"1342", "1234567")
        miembro2 = Miembro("Pedro", "BSU", "pusb@hotmail.com" ,"1432", "1243567")

        self.comite.addMiembro(miembro1)
        self.comite.addMiembro(miembro2)

        assert not self.comite.setPresi(presi), "Coloco como presi un no miembro"

        self.comite.addMiembro(presi)
        assert self.comite.setPresi(presi) and self.comite.presi == presi,\
            "Fallo colocando como presi a alguien que acabo de agregar"

        for x in self.comite.miembros:
            assert self.comite.setPresi(x) and self.comite.presi == x,\
                "Falla colocando como presi a un miembro cualquiera"

class pruebaCLEI(unittest.TestCase):

    def setUp(self):
        self.clei = CLEI()

    def testAddComites(self):
        
        for i in range(0,100):
            self.clei.addComites("topico"+str(i))
            
            assert len(self.clei.comites) == self.clei.numComi,\
                "No se estan agregando comite "+str(i)

    def testSetPresidente(self):

        self.clei.addComites("topico")
        self.clei.addMiembro('1',"Jose", "USB", "jusb@hotmail.com","1342"\
                                 , "1234567")

        assert self.clei.setPresidente('1',self.clei.comites['1'].miembros[0]),\
            "No esta agregando presidente"

        
    def testAddMiembro(self):

        self.clei.addComites("topico")
        comitePrueba = ComitePrograma()
        comitePrueba.topicos.append("topico")

        for i in range(0,3):
            miembro = Miembro("Jose"+str(i), "USB", "jusb"+str(i)+\
                                  "@hotmail.com",str(i)+"-1342", str(i)+\
                                  "1234567")
            comitePrueba.miembros.append(miembro)
            self.clei.addMiembro('1',"Jose"+str(i), "USB", "jusb"+str(i)+\
                                     "@hotmail.com",str(i)+"-1342", str(i)+\
                                     "1234567")

        presi = self.clei.comites['1'].miembros[1]
        comitePrueba.presi = presi
        self.clei.comites['1'].setPresi(presi)

        assert str(comitePrueba) == str(self.clei.comites['1']),\
            "No se estan creando bien los comites"

        
if __name__=="__main__":
    unittest.main()

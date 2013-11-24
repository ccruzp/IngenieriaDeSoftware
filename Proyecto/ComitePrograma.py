#!/usr/bin/python
# -*- coding: utf-8 -*-

# Miembro.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que representa los Comite de Programa del CLEI

class ComitePrograma(object):

    def __init__(self):
        self.miembros = []
        self.presi = None
        self.topicos = []

    def addMiembro(self, miembro):
        self.miembros.append(miembro)

    def setPresi(self, miembro):
        if miembro in self.miembros:
            self.presi = miembro
            return True
        
        return False

    def __str__(self):
        miembros = ""

        for x in self.miembros:
            miembros += str(x)+'\n'
        
        return "Topicos:\n"+str(self.topicos)+"\nPresidente:\n"+str(self.presi)\
            +"\nMiembros:\n"+miembros

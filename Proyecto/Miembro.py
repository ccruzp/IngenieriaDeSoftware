#!/usr/bin/python
# -*- coding: utf-8 -*-

# Miembro.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que representa miembros de Comite de Programa en CLEI

from Persona import *

class Miembro(Persona):
    
    def __init__(self, nombre, inst, correo, dirpost, numero, url=None):
         Persona.__init__(self, nombre, inst, correo, dirpost, numero, url)
         self.experticia = []

    def __str__(self):
        return Persona.__str__(self)+'\t'+str(self.experticia)

if __name__=="__main__":
    miembro1 = Miembro("Jose", "USB", "jusb@hotmail.com" ,"1342", "1234567")
    miembro2 = Miembro("Jose", "USB", "jusb@hotmail.com" ,"1342", "1234567", "usb.com")

    miembro1.experticia.append("IA")
    miembro1.experticia.append("BD")
    miembro1.experticia.append("IS")
    miembro1.experticia.append("OP")

    miembro2.experticia.append("IA")
    miembro2.experticia.append("BD")
    miembro2.experticia.append("IS")
    miembro2.experticia.append("OP")

    print miembro1
    print "________________________________________________"
    print miembro2

    

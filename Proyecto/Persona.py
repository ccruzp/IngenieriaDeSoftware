#!/usr/bin/python
# -*- coding: utf-8 -*-

# Persona.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que representa personas del CLEI

class Persona(object):

    def __init__(self, nombre, inst, correo, dirpost, numero, url=None):
        self.nombre = nombre
        self.institucion = inst
        self.correo = correo
        self.dirPostal = dirpost
        self.urlWeb = url
        self.telefono = numero

    def __str__(self):

        if self.urlWeb == None:
            return self.nombre+'\t'+self.institucion+'\t'+self.correo+'\t'\
                +self.dirPostal+'\t'+self.telefono
        else:
            return self.nombre+'\t'+self.institucion+'\t'+self.correo+'\t'\
                +self.dirPostal+'\t'+self.telefono+'\t'+self.urlWeb

if __name__=="__main__":
    persona1 = Persona("Jose", "USB", "jusb@hotmail.com" ,"1342", "1234567")
    persona2 = Persona("Jose", "USB", "jusb@hotmail.com" ,"1342", "1234567", "usb.com")

    print persona1
    print "________________________________________________"
    print persona2

#!/usr/bin/python
# -*- coding: utf-8 -*-

# main.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463

# Main principal del sistema para CLEI

from CLEI import *

def crearArticulo():
    nombreArticulo = raw_input("\nInserte Titulo:")
    temaArticulo = raw_input("Inserte Topico:")
    CLEI.nuevoArticulo(nombreArticulo,temaArticulo)
    print 'El articulo "'+nombreArticulo+'" se agrego correctamente!'
    raw_input("Presione enter para continuar")

def crearMiembro():
    comite = raw_input("\nInserte el numero del comite:")
    nombreMiembro = raw_input("Inserte el nombre del miembro:")
    institucionMiembro = raw_input("Inserte la intitucion del miembro:")
    correoMiembro = raw_input("Inserte el correo del miembro:")
    dirpostalMiembro = raw_input("Inserte la direccion postal del miembro:")
    telefonoMiembro = raw_input("Inserte el numero de telefono del miembro:")
    urlMiembro = raw_input('Inserte el URL del miembro, si no tiene inserte "n":')
    
    if urlMiembro == 'n' or urlMiembro == 'N':
        urlMiembro = None

    if not CLEI.addMiembro(comite, nombreMiembro, institucionMiembro,\
                               correoMiembro, dirpostalMiembro, telefonoMiembro,\
                               urlMiembro):
        print "Comite "+comite+" no existe"+\
            ", necesita crearlo antes de agregar miembros!"
    else:
        print 'El miembro "'+nombreMiembro+'" se agrego correctamente!'

    raw_input("Presione enter para continuar")

def crearComite():
    topico = raw_input("\nInserte el topico:")
    
    CLEI.addComites(topico)

    print 'El comite sobre el topico "'+topico+'" se agrego correctamente!'

    raw_input("Presione enter para continuar")
    
def colocarPresidente():
    comite = raw_input("\nInserte el numero del comite:")
    presidente = raw_input("Inserte el miembro que sera preidente:")
    
    try:
        CLEI.comites[comite].setPresi(presidente)
        print 'El miembro "'+presidente+'" ahora es el presidente de comite '\
            +comite+'!'
    
    except KeyError, e:
        print "Comite "+comite+" no existe!"
        
    raw_input("Presione enter para continuar")


def imprimirTodo ():
    print '\n', CLEI, '\n'
    raw_input("Presione enter para continuar")

def salir():
    print "\n\n\t\tHasta luego\n\n"
    exit()

menu = {   '1':crearArticulo,
           '2':crearMiembro,
           '3':crearComite,
           '4':colocarPresidente,
           '5':imprimirTodo,
           '0':salir
           }

CLEI = CLEI()

print "\n\tBienvenido al Sistema del CLEI\n"

while True:
    print "\nOpciones\n"+"\n1: crear Articulo\n"+"\n2: crear Miembro\n"+\
        "\n3: crear Comite\n"+"\n4: colocar Presidente\n"+"\n5: imprimir Todo\n"+"\n0:Salir\n"
    opcion = -1
    while opcion not in range(0,len(menu)+1):
        opcion = input("Por favor seleccione una opcion: ")
    
    menu[str(opcion)]()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


#######################################################
#                                                     #
# descomponerPrimos.py                                #
# Recibe un numero y lo descompone en factores primos #
# Autores: Carlos Cruz 10-10168                       #
#          Luis Miranda 10-10463                      #
#                                                     #
#######################################################

numero = int(raw_input("Introduzca un numero positivo mayor que 1: "))
primo = 2

if numero <= 0:
    print "El numero no es positivo"
elif numero == 1:
    print "El uno no se puede descomponer en factores primos"
else:
    print "El numero " + str(numero) + " se descompone en: "

    while numero > 1:
        numVeces = 0
        while (numero % primo)== 0:
            numVeces += 1
            numero /= primo
        if numVeces > 0:
            print "El numero primo " + str(primo),
            print "aparece " + str(numVeces),
        
            if numVeces == 1:
                print "vez"
            else:
                print "veces"
        primo += 1



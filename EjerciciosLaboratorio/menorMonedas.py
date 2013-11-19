#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################
#                                                            #
# menorMonedas.py                                            #
#                                                            #
# Carlos Cruz 10-10168                                       #
# Luis Miranda 10-10463                                      #
#                                                            #
##############################################################


import sys

try:
    monto = int(sys.argv[1])
    monedas = tuple(int(x.strip()) for x in sys.argv[2].split(','))
except:
    print "./menorMonedas.py montoDinero moneda1,moneda2,...,monedaN"
    exit(1)

monedas = sorted(monedas, reverse=True)

for x in monedas:
    dummy = monto//x
    print x, ':\t', dummy
    monto = monto % x

if monto > 0:
    print 'Existe un monto de', monto, 'que no se puede representar'

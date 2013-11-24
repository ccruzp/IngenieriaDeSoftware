#!/usr/bin/python
# -*- coding: utf-8 -*-

# Articulo.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que representa los articulos del CLEI

class Articulo(object):
           
    # Constructor
    def __init__(self, titulo, tema):
        self.titulo = titulo
        self.tema = tema
        self.aceptado = False
        self.calificacion = []

    # Calcula el promedio de las calificaciones del articulo    
    def promedioEvaluaciones(self):
        if len(self.calificacion) == 0:
            return 0
        else:
            promedio = 0
            for nota in self.calificacion:
                promedio += nota
                
            promedio = promedio / float(len(self.calificacion))
            return promedio

    # Agrega una nota a la calificacion del articulo
    def calificar(self, nota):
        self.calificacion.append(nota)
    
    # Metodo que verifica si un articulo esta o no aceptado
    def verificarAceptacion(self):
        if len(self.calificacion) >= 2:
            self.aceptado = self.promedioEvaluaciones() >= 3            
        return self.aceptado

    # Funciona como el toString de Java
    def __str__(self):
        return self.tema+' '+self.titulo+': '+str(self.calificacion)

# En la internet en todos lados sale esto xD
if __name__=="__main__":
    print "Hola"
    articulo = Articulo("Articulo de prueba", "Pruebas")
    print articulo.tema, articulo.titulo
    print articulo
    articulo.calificar(0)
    articulo.calificar(0)
    print articulo.calificacion, articulo.calificacion == [0,0]
    print articulo.promedioEvaluaciones()
    articulo.verificarAceptacion()
    print articulo
    print articulo.aceptado

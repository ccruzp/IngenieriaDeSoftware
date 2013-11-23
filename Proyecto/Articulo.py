# Articulo.py
# Autores: Carlos Cruz 10-10168
#          Luis Miranda 10-10463
# Clase que representa los articulos del CLEI

class Articulo(object):
    titulo = None
    tema = None
    aceptado = False
    calificacion = []
        
    # Constructor
    def __init__(self, titulo, tema):
        self.titulo = titulo
        self.tema = tema
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
        if self.promedioEvaluaciones() >= 3:
            self.aceptado = True

print "Hola"
articulo = Articulo("Articulo de prueba", "Pruebas")
print articulo.tema, articulo.titulo
articulo.calificar(0)
articulo.calificar(0)
print articulo.calificacion
print articulo.promedioEvaluaciones()
articulo.verificarAceptacion()
print articulo.aceptado
#Cree una clase Punto que represente un punto en el plano cartesiano.
#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
from math import sqrt

class punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mostrar(self):
        print(f"el punto se encuentra en ({self.x},{self.y})")
    def mover(self,x,y):
        self.x = x
        self.y = y
    def calcular_distancia(self,punto2):
        distancia = sqrt((punto2.x-self.x)**2+(punto2.y-self.y)**2)
        print (distancia)


punto1 = punto(4,5)
punto2 = punto(1,1)

punto1.mostrar()
punto1.calcular_distancia(punto2)


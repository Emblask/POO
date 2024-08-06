#Cree una clase Punto que represente un punto en el plano cartesiano.
#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
from math import sqrt, pi

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

punto1 = punto(1,2)
punto2 = punto(4,5)

#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas.
# Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

class rectangulo:
    def __init__(self,esquina1,esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2
    def perimetro(self):
        base = abs(self.esquina2.x-self.esquina1.x)
        altura = abs(self.esquina2.y-self.esquina1.y)
        return (2*(base+altura))
    def area(self):
        base = abs(self.esquina2.x-self.esquina1.x)
        altura = abs(self.esquina2.y-self.esquina1.y)
        return (base*altura)
    def cuadrado(self):
        base = abs(self.esquina2.x-self.esquina1.x)
        altura = abs(self.esquina2.y-self.esquina1.y)
        if base == altura:
            print ("Es un cuadrado")
        else:
            print ("Es un rectangulo")


# Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. 
# Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

class circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    def area(self):
        return (pi*(self.radio**2))
    def perimetro(self):
        return (pi*(self.radio*2))
    def punto_en_circulo(self, punto):
        centro_punto = sqrt((self.centro.x-punto.x)**2+(self.centro.y-punto.y)**2)
        if centro_punto > self.radio:
            print (f"el punto se encuentra fuera de la circunferencia")
        else:
            print (f"el punto pertenece a la circunferencia")
    





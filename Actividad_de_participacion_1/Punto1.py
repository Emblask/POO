#Escribir una función que calcule el área de un círculo dado su radio

from math import pi

def area_circulo(radio):
    return (pi*(radio**2))

radio = float(input("ingrese el radio del circulo "))
print (f" el area de un circulo de radio {radio} es de {area_circulo(radio)}")
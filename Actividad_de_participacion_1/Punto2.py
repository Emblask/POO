#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

from random import randint

def lista_random():
    alea =[]
    cantidad = int(randint(50,100))
    for i in range(1,cantidad):
        alea.append(randint(1,100))
    print (alea)

lista_random()
#Crear un programa que genere una matriz de números y la imprima en pantalla.

from numpy import array
from random import randint

def matriz5x5():
    matriz=[]
    for i in range(0,5):
        lista = []
        for j in range (0,5):
            lista.append(randint(1,10))
        matriz.append(lista)
    matriz =array(matriz)
    return (matriz)


print(matriz5x5())
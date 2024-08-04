#Crear un programa que calcule la suma de los números en una lista dada.

def suma(lista):
    total = 0
    for i in lista:
        total += i
    return total


lista = [1,2,3,4,5,6,7,8,9]
print(suma(lista))
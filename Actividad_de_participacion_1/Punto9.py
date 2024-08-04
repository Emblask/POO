#Escribir una función que calcule el factorial de un número dado.

def fact(numero):
    total= 1
    for i in range (2,numero+1):
        total = total*i
    return total


print(fact(8))
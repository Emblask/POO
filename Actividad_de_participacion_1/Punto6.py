#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

def menor_mayor(lista):
    lista.sort()
    return (lista[0], lista[-1])


lista = [5,2,3,5,2,7,17,8,1,3]
print(menor_mayor(lista))
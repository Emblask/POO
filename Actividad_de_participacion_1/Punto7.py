#Crear una función que invierta el orden de los elementos en una lista dada.

def invertir(lista):
    lista.reverse()
    return (lista)


lista = [5,2,3,5,2,7,17,8,1,3]
print(invertir(lista))
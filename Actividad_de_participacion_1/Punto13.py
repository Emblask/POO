#Escribir una función que calcule la media aritmética de una lista de números

def media(lista):
    total = 0
    for i in lista:
        total+=i
    return (total/len(lista))

lista = [1,2,3,4,5,6,7,8]
print(media(lista))
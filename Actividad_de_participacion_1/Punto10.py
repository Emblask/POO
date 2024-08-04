#Crear un programa que genere una lista de números pares entre 1 y 100.

def lista_par():
    lista= []
    for i in range (1,101):
        if i%2==0:
            lista.append(i)
    return lista


print(lista_par())
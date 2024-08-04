#Escribir un programa que determine si un número dado es par o impar.

def par_impar(numero):
    if numero%2==0:
        print (f"el numero {numero} es par")
    else:
        print(f"el numero {numero} es impar")

numero = int(input("ingrese el numero "))
par_impar(numero)
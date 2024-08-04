#Crear un programa que pida al usuario ingresar una cadena de texto
#y determine si es un palíndromo o no.

def palindromo():
    frase = (input("ingrese la frase a evaluar "))
    frase = frase.lower()
    frase = frase.replace(" ","")
    reves = frase[::-1]
    if frase==reves:
        print ("es un palindromo")
    else:
        print("NO es un palindromo")

palindromo()
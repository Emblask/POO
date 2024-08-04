#Crear un programa que pida al usuario ingresar dos números y 
#calcule su suma, resta, multiplicación y división.

def operaciones():
    num1 = float(input("ingrese un numero "))
    num2 = float(input("ingrese otro numero "))
    print (f"la suma es {num1+num2}")
    print (f"la resta es {num1-num2}")
    print (f"la multiplicación es {num1*num2}")
    print (f"la division es {num1/num2}")

operaciones()
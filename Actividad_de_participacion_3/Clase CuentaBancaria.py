# Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance.
# Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    def depositar(self, cantidad):
        self.balance += cantidad
    def retirar(self, cantidad):
        self.balance -= cantidad
    def aplicar_cuota_manejo(self):
        self.balance -= (self.balance*0.02)
    def mostrar_detalles(self):
        print(self.numero_cuenta)
        print(self.propietarios)
        print(self.balance)

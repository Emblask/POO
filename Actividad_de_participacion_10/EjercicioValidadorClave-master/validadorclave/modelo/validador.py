# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod
from errores import *

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError("La clave no cumple con la longitud mínima requerida")

    def _contiene_mayuscula(self, clave):
        if not any(char.isupper() for char in clave):
            raise NoTieneLetraMayusculaError("La clave no contiene una letra mayúscula")

    def _contiene_minuscula(self, clave):
        if not any(char.islower() for char in clave):
            raise NoTieneLetraMinusculaError("La clave no contiene una letra minúscula")

    def _contiene_numero(self, clave):
        if not any(char.isdigit() for char in clave):
            raise NoTieneNumeroError("La clave no contiene un número")

    @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def _contiene_caracter_especial(self, clave):
        if not any(char in "@_#$%" for char in clave):
            raise NoTieneCaracterEspecialError("La clave no contiene un caracter especial válido")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self._contiene_caracter_especial(clave)
        return True

# Clase para la validación de Calisto
class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def _contiene_calisto(self, clave):
        posicion = clave.lower().find("calisto")
        if posicion == -1:
            raise NoTienePalabraSecretaError("La clave no contiene la palabra 'calisto'")
        
        palabra = clave[posicion:posicion + 7]
        mayusculas = sum(1 for c in palabra if c.isupper())
        
        if mayusculas < 2 or mayusculas == len(palabra):
            raise NoTienePalabraSecretaError("La palabra 'calisto' debe tener al menos dos letras en mayúscula, pero no todas")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self._contiene_calisto(clave)
        return True

# Clase Validador que utiliza una regla específica para validar la clave
class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
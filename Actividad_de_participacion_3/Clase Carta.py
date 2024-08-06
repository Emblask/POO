# Cree una clase Carta que contenga dos propiedades valor y pinta, 
# las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). 
# Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class carta:
    
    trebol = "trebol"
    diamante = "diamante"
    corazon = "corazon"
    pica = "pica"
    
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = carta("10",carta.trebol)

print(carta1.pinta)
    
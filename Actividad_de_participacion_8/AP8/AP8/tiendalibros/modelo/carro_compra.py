class CarroCompras:
    def __init__(self)
        self.item:list[ItemCompra] = []

    def agregar_item(self, libro: Libro, cantidad: int) -> ItemCompra:
        return ItemCompra(libro, cantidad)


    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self.item)

    def quitar_item(self, isbn: str) -> None:
        self.item.pop(item for item in self.item if item.libro.isbn == isbn)

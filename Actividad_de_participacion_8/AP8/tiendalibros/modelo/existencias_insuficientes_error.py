from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo: str, isbn: str, cantidad_a_comprar: int, existencias_disponibles: int):
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias_disponibles = existencias_disponibles
        mensaje = (f"El libro con titulo {titulo} y isbn {isbn} no tiene suficientes existencias. "
                   f"Cantidad solicitada: {cantidad_a_comprar}, existencias disponibles: {existencias_disponibles}")
        super().__init__(mensaje)

    def __str__(self):
        return (f"El libro con titulo {self.titulo} y isbn {self.isbn} no tiene suficientes existencias para la compra. "
                f"Cantidad a comprar: {self.cantidad_a_comprar}, existencias disponibles: {self.existencias_disponibles}")
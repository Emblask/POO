from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self, titulo: str, isbn: str):
        self.titulo = titulo
        self.isbn = isbn
        mensaje = f"El libro con titulo {titulo} y isbn {isbn} está agotado"
        super().__init__(mensaje)

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} está agotado"

import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        libro = input("Ingrese el ISBN del libro a retirar: ")
        tienda_libros.retirar_item_de_carrito(libro)
        print("Libro retirado del carrito de compras")
    
def agregar_libro_a_carrito_de_compras(self):
    try:
        libro = input("Ingrese el ISBN del libro a agregar: ")
        cantidad = int(input("Ingrese la cantidad del libro: "))
        tienda_libros.agregar_item_a_carrito(libro, cantidad)
        print("Libro agregado al carrito de compras")
    
    except LibroAgotadoError as e:
        print(f"Error: {e}")
    
    except ValueError:
        print("Error: La cantidad ingresada debe ser un número entero válido.")
    
    except KeyError:
        print("Error: El libro ingresado no existe en el catálogo.")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def adicionar_un_libro_a_catalogo(self):
    try:
        libro = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el título del libro: ")
        precio = float(input("Ingrese el precio del libro: "))
        existencias = int(input("Ingrese las existencias del libro: "))
        tienda_libros.adicionar_libro_a_catalogo(libro, titulo, precio, existencias)
        print("Libro agregado al catálogo")
    
    except LibroExistenteError as e:
        print(f"Error: {e}")
    
    except ValueError:
        print("Error: Por favor ingrese un precio o cantidad válidos (números).")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
          


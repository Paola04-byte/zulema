import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    # ---------------------------
    # CARGAR INVENTARIO
    # ---------------------------
    def cargar_inventario(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                print("Archivo de inventario creado correctamente.")

            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        codigo, nombre, cantidad, precio = datos
                        self.productos[codigo] = Producto(
                            codigo, nombre, int(cantidad), float(precio)
                        )
            print("Inventario cargado correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para acceder al archivo.")
        except Exception as e:
            print("Error inesperado al cargar el inventario:", e)

    # ---------------------------
    # GUARDAR INVENTARIO
    # ---------------------------
    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(str(producto) + "\n")
            return True
        except PermissionError:
            print("Error: Permiso denegado al guardar el archivo.")
            return False
        except Exception as e:
            print("Error inesperado al guardar:", e)
            return False

    # ---------------------------
    # AÑADIR PRODUCTO
    # ---------------------------
    def añadir_producto(self, codigo, nombre, cantidad, precio):
        if codigo in self.productos:
            print("El producto ya existe.")
            return

        self.productos[codigo] = Producto(codigo, nombre, cantidad, precio)
        if self.guardar_inventario():
            print("Producto añadido y guardado exitosamente.")

    # ---------------------------
    # ACTUALIZAR PRODUCTO
    # ---------------------------
    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        if codigo not in self.productos:
            print("Producto no encontrado.")
            return

        if cantidad is not None:
            self.productos[codigo].cantidad = cantidad
        if precio is not None:
            self.productos[codigo].precio = precio

        if self.guardar_inventario():
            print("Producto actualizado correctamente.")

    # ---------------------------
    # ELIMINAR PRODUCTO
    # ---------------------------
    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            if self.guardar_inventario():
                print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # ---------------------------
    # BUSCAR PRODUCTO
    # ---------------------------
    def buscar_producto(self, codigo):
        if codigo in self.productos:
            p = self.productos[codigo]
            print(f"Código: {p.codigo}")
            print(f"Nombre: {p.nombre}")
            print(f"Cantidad: {p.cantidad}")
            print(f"Precio: {p.precio}")
        else:
            print("Producto no encontrado.")


# ---------------------------
# INTERFAZ DE USUARIO
# ---------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(codigo, nombre, cantidad, precio)

        elif opcion == "2":
            codigo = input("Código del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(codigo, cantidad, precio)

        elif opcion == "3":
            codigo = input("Código del producto: ")
            inventario.eliminar_producto(codigo)

        elif opcion == "4":
            codigo = input("Código del producto: ")
            inventario.buscar_producto(codigo)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
# Clase que representa un producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_producto(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}"


# Clase que representa una tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Tienda: {self.nombre}")
        for producto in self.productos:
            print(producto.mostrar_producto())


# Uso de las clases
producto1 = Producto("Arroz", 2.50)
producto2 = Producto("Azúcar", 1.80)

tienda = Tienda("Mini Market Central")
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

tienda.mostrar_productos()


import json
import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = []
        self.cargar_datos()

    # Guardar productos en JSON
    def guardar_datos(self):
        with open(self.archivo, "w") as f:
            json.dump([p.to_dict() for p in self.productos], f, indent=4)

    # Cargar productos desde JSON
    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.productos = [Producto.from_dict(p) for p in datos]

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: ID duplicado.")
                return
        self.productos.append(producto)
        self.guardar_datos()
        print("✅ Producto agregado.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_datos()
                print("✅ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_datos()
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)

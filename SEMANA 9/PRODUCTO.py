class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio

    # Convertir objeto a diccionario (para guardar en JSON)
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    # Crear objeto desde diccionario
    @staticmethod
    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"

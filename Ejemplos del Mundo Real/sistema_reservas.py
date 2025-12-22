# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"


# Clase que representa una reserva
class Reserva:
    def __init__(self, cliente, fecha, lugar):
        self.cliente = cliente
        self.fecha = fecha
        self.lugar = lugar

    def confirmar_reserva(self):
        print("Reserva confirmada")
        print(self.cliente.mostrar_info())
        print(f"Fecha: {self.fecha}")
        print(f"Lugar: {self.lugar}")


# Uso de las clases
cliente1 = Cliente("Juan Pérez", "0102030405")
reserva1 = Reserva(cliente1, "15/08/2025", "Hotel Central")

reserva1.confirmar_reserva()

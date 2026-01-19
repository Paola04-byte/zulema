# ============================
# CLASE BASE
# ============================
class Empleado:
    """
    Clase base que representa a un empleado genérico.
    """

    def __init__(self, nombre, salario_base):
        # Atributo público
        self.nombre = nombre

        # Atributo privado (encapsulación)
        self.__salario_base = salario_base

    # Método getter para acceder al salario base
    def get_salario_base(self):
        return self.__salario_base

    # Método setter para modificar el salario base
    def set_salario_base(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario_base = nuevo_salario
        else:
            print("El salario debe ser mayor que 0")

    # Método que será sobrescrito (polimorfismo)
    def calcular_salario(self):
        return self.__salario_base

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Salario: {self.calcular_salario()}")


# ============================
# CLASE DERIVADA
# ============================
class EmpleadoTiempoCompleto(Empleado):
    """
    Clase derivada que representa a un empleado de tiempo completo.
    Hereda de la clase Empleado.
    """

    def __init__(self, nombre, salario_base, bono):
        # Llamada al constructor de la clase base
        super().__init__(nombre, salario_base)
        self.bono = bono

    # Sobrescritura del método (polimorfismo)
    def calcular_salario(self):
        return self.get_salario_base() + self.bono


# ============================
# PROGRAMA PRINCIPAL
# ============================
def main():
    # Crear instancia de la clase base
    empleado1 = Empleado("Ana", 1200)

    # Crear instancia de la clase derivada
    empleado2 = EmpleadoTiempoCompleto("Carlos", 1200, 300)

    # Demostración de encapsulación
    empleado1.set_salario_base(1300)

    # Uso del polimorfismo
    empleados = [empleado1, empleado2]

    for empleado in empleados:
        empleado.mostrar_info()


# Punto de entrada del programa
if __name__ == "__main__":
    main()

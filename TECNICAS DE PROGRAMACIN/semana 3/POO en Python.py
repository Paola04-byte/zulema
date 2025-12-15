# -------------------------------------------------
# Programa: Promedio semanal de temperaturas
# Paradigma: Programación Orientada a Objetos (POO)
# -------------------------------------------------

class Clima:
    """
    Clase que representa la información climática semanal.
    Aplica encapsulamiento usando atributos privados.
    """

    def __init__(self):
        # Encapsulamiento: atributo privado
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        """
        Método que calcula el promedio semanal.
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)


# Programa principal
clima_semanal = Clima()
clima_semanal.ingresar_temperaturas()
promedio = clima_semanal.calcular_promedio_semanal()

print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

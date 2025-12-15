# ---------------------------------------------
# Programa: Promedio semanal de temperaturas
# Paradigma: Programación Tradicional
# ---------------------------------------------

def ingresar_temperaturas():
    """
    Función que solicita al usuario ingresar
    las temperaturas de 7 días.
    Retorna una lista de temperaturas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio semanal
    a partir de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal que organiza la ejecución
    del programa.
    """
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()

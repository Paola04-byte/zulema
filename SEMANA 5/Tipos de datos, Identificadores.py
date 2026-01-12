"""
Programa: Cálculo del área y perímetro de un rectángulo
Descripción:
Este programa solicita al usuario el ancho y el alto de un rectángulo,
valida que los valores sean positivos y calcula su área y perímetro.
"""

# Función para calcular el área del rectángulo
def calcular_area(ancho, alto):
    return ancho * alto


# Función para calcular el perímetro del rectángulo
def calcular_perimetro(ancho, alto):
    return 2 * (ancho + alto)


# Programa principal
def main():
    # Solicitar datos al usuario (tipo float)
    ancho = float(input("Introduce el ancho del rectángulo: "))
    alto = float(input("Introduce el alto del rectángulo: "))

    # Validación de datos (tipo boolean)
    datos_validos = ancho > 0 and alto > 0

    if datos_validos:
        # Cálculos
        area = calcular_area(ancho, alto)
        perimetro = calcular_perimetro(ancho, alto)

        # Mostrar resultados (uso de string)
        print(f"El área del rectángulo es: {area}")
        print(f"El perímetro del rectángulo es: {perimetro}")
    else:
        print("Error: El ancho y el alto deben ser valores positivos.")


# Llamada al programa principal
main()

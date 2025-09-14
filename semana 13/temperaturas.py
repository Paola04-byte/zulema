def calcular_promedios(temperaturas):
    """
    Calcula el promedio de temperaturas por ciudad.

    Parámetros:
        temperaturas (dict): Diccionario con formato
            {
                "Ciudad": [[semana1], [semana2], ...]
            }
            Cada semana es una lista de temperaturas diarias.

    Retorna:
        dict: Promedio de temperaturas por ciudad.
    """
    promedios = {}
    for ciudad, semanas in temperaturas.items():
        total = 0
        conteo = 0
        for semana in semanas:
            total += sum(semana)
            conteo += len(semana)
        promedios[ciudad] = round(total / conteo, 2)
    return promedios


# Datos de ejemplo: temperaturas (°C) de 3 ciudades amazónicas en 4 semanas
datos_temperaturas = {
    "Tena": [
        [25, 26, 24, 25, 26, 27, 25],  # Semana 1
        [26, 25, 24, 26, 27, 28, 25],  # Semana 2
        [27, 26, 25, 26, 27, 26, 25],  # Semana 3
        [26, 25, 24, 25, 26, 27, 24]  # Semana 4
    ],
    "Puyo": [
        [23, 24, 23, 25, 24, 23, 22],
        [24, 25, 23, 24, 23, 25, 24],
        [25, 24, 24, 23, 24, 25, 24],
        [23, 24, 23, 22, 24, 23, 23]
    ],
    "Macas": [
        [22, 23, 22, 21, 23, 22, 21],
        [23, 22, 22, 23, 21, 22, 22],
        [22, 23, 21, 22, 23, 22, 21],
        [23, 22, 21, 22, 21, 23, 22]
    ]
}

# Calcular promedios
promedios = calcular_promedios(datos_temperaturas)

# Mostrar resultados
for ciudad, promedio in promedios.items():
    print(f"El promedio de {ciudad} es: {promedio} °C")

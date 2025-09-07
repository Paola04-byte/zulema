import random

# Nuevas ciudades
ciudades = ["Loja", "Ambato", "Esmeraldas", "Manta"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2

# Crear matriz 3D [ciudad][día][semana]
matriz_temperaturas = [[[random.randint(15, 32) for _ in range(num_semanas)]
                        for _ in range(len(dias))]
                        for _ in range(len(ciudades))]

# Mostrar datos generados
print("=== Datos de temperaturas ===")
for c in range(len(ciudades)):
    for s in range(num_semanas):
        print(f"\nCiudad: {ciudades[c]}, Semana {s+1}")
        for d in range(len(dias)):
            print(f"{dias[d]}: {matriz_temperaturas[c][d][s]} °C")

# Calcular promedios semanales por ciudad
print("\n=== Promedio de temperaturas por ciudad y semana ===")
for c in range(len(ciudades)):
    for s in range(num_semanas):
        suma = 0
        for d in range(len(dias)):
            suma += matriz_temperaturas[c][d][s]
        promedio = suma / len(dias)
        print(f"Ciudad: {ciudades[c]}, Semana {s+1} → Promedio: {promedio:.2f} °C")

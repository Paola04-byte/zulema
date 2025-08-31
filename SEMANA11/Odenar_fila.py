def bubble_sort(arr):
    """Implementa el algoritmo Bubble Sort para ordenar una lista."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def ordenar_fila(matriz, numero_fila):
    """Ordena una fila específica de la matriz en orden ascendente."""
    if 0 <= numero_fila < len(matriz):
        matriz[numero_fila] = bubble_sort(matriz[numero_fila])
        return matriz
    else:
        print("El número de fila es inválido.")
        return matriz

def imprimir_matriz(matriz):
    """Imprime la matriz de forma legible."""
    for fila in matriz:
        print(fila)

# Matriz bidimensional de ejemplo (3x3)
matriz_original = [
    [5, 2, 8],
    [1, 9, 4],
    [7, 3, 6]
]

print("Matriz Original:")
imprimir_matriz(matriz_original)

# Ordenar la segunda fila (índice 1)
fila_a_ordenar = 1
matriz_ordenada = ordenar_fila(matriz_original.copy(), fila_a_ordenar) # Usar copia para no modificar la original

print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
imprimir_matriz(matriz_ordenada)


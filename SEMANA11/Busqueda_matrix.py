matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
def buscar_valor(matriz_busqueda, valor_a_buscar):
    for indice_fila, fila in enumerate(matriz_busqueda):
        for indice_columna, elemento in enumerate(fila):
            if elemento == valor_a_buscar:
                return True, indice_fila, indice_columna  # Valor encontrado
    return False, -1, -1  # Valor no encontrado
valor_buscado = 5  # Define el valor que quieres buscar
encontrado, fila, columna = buscar_valor(matriz, valor_buscado)

if encontrado:
    print(f"El valor {valor_buscado} se encontró en la posición: Fila {fila}, Columna {columna}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")

valor_buscado_no_encontrado = 10
encontrado, fila, columna = buscar_valor(matriz, valor_buscado_no_encontrado)

if encontrado:
    print(f"El valor {valor_buscado_no_encontrado} se encontró en la posición: Fila {fila}, Columna {columna}")
else:
    print(f"El valor {valor_buscado_no_encontrado} no se encontró en la matriz.")
    

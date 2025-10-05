# --------------------------------------------
# Tarea: Trabajo con Archivos de Texto en Python
# Autor: Zulema
# Fecha: 05/10/2025
# --------------------------------------------

# ------------------------------
# ESCRITURA DE ARCHIVO DE TEXTO
# ------------------------------

# Abrimos (o creamos si no existe) el archivo "my_notes.txt" en modo escritura ('w')
# El modo 'w' sobrescribe el contenido si el archivo ya existe
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Nota 1: Hoy aprendí a manejar archivos de texto en Python.\n")
    file.write("Nota 2: Es importante cerrar los archivos después de usarlos.\n")
    file.write("Nota 3: El uso de 'with open()' facilita el manejo seguro de archivos.\n")

# El archivo se cierra automáticamente al salir del bloque 'with'


# ------------------------------
# LECTURA DE ARCHIVO DE TEXTO
# ------------------------------

# Abrimos el archivo en modo lectura ('r')
with open("my_notes.txt", "r") as file:
    # Leemos el contenido línea por línea
    print("Contenido del archivo my_notes.txt:\n")

    # Usamos un bucle para leer cada línea con readline()
    line = file.readline()  # Leemos la primera línea
    while line:  # Mientras haya contenido
        print(line.strip())  # Mostramos la línea (sin salto de línea extra)
        line = file.readline()  # Leemos la siguiente línea

# El archivo se cierra automáticamente al finalizar el bloque 'with'


# ------------------------------
# FIN DEL PROGRAMA
# ------------------------------
print("\nEl archivo se ha leído y cerrado correctamente.")

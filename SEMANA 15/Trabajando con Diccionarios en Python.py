# Crear un diccionario con información personal de Paola
informacion_personal = {
    "nombre": "Paola Unup",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Analista de Datos"
}

# Modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"

# Actualizar la profesión
informacion_personal["profesion"] = "Ingeniera de Software"

# Verificar si la clave 'telefono' existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593-99-987-6543"  # número ficticio

# Eliminar la clave 'edad'
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)

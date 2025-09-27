informacion_personal = {
    "nombre": "María García",
    "edad": 29,
    "ciudad": "Quito",
    "profesion": "Analista de Sistemas"
}

# Modificar ciudad
informacion_personal["ciudad"] = "Guayaquil"

# Actualizar/asegurar profesión
informacion_personal["profesion"] = "Ingeniera de Software"

# Agregar teléfono si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593-99-123-4567"

# Eliminar edad
informacion_personal.pop("edad", None)

# El diccionario final queda en la variable 'informacion_personal' sin mostrarse

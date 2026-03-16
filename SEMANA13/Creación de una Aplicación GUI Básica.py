# Importar la librería Tkinter
import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_dato():
    dato = entrada.get()  # Obtener texto del campo

    if dato != "":
        lista.insert(tk.END, dato)  # Insertar en la lista
        entrada.delete(0, tk.END)   # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")
ventana.geometry("400x300")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar Lista", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
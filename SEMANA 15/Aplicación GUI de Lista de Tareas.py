import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Lista para almacenar tareas (texto + estado)
tareas = []


# ---------------- FUNCIONES ----------------

def agregar_tarea(event=None):
    """Agrega una nueva tarea a la lista"""
    tarea = entrada.get().strip()

    if tarea == "":
        messagebox.showwarning("Advertencia", "Debe escribir una tarea")
        return

    tareas.append({"texto": tarea, "completada": False})
    actualizar_lista()
    entrada.delete(0, tk.END)


def marcar_completada():
    """Marca la tarea seleccionada como completada"""
    seleccion = lista.curselection()

    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")
        return

    indice = seleccion[0]
    tareas[indice]["completada"] = True
    actualizar_lista()


def eliminar_tarea():
    """Elimina la tarea seleccionada"""
    seleccion = lista.curselection()

    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")
        return

    indice = seleccion[0]
    tareas.pop(indice)
    actualizar_lista()


def actualizar_lista():
    """Actualiza visualmente la lista de tareas"""
    lista.delete(0, tk.END)

    for tarea in tareas:
        if tarea["completada"]:
            lista.insert(tk.END, "✔ " + tarea["texto"])
        else:
            lista.insert(tk.END, tarea["texto"])


def doble_click(event):
    """Evento opcional: marcar tarea como completada con doble clic"""
    seleccion = lista.curselection()

    if seleccion:
        indice = seleccion[0]
        tareas[indice]["completada"] = True
        actualizar_lista()


# ---------------- INTERFAZ ----------------

# Campo de entrada
entrada = tk.Entry(root, width=40)
entrada.pack(pady=10)

# Evento Enter para agregar tarea
entrada.bind("<Return>", agregar_tarea)

# Botones
btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista = tk.Listbox(root, width=50, height=10)
lista.pack(pady=10)

# Evento opcional: doble clic
lista.bind("<Double-Button-1>", doble_click)

# Ejecutar aplicación
root.mainloop()
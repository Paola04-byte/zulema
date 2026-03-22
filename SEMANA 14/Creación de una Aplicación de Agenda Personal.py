import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesita instalar: pip install tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Eventos")
        self.root.geometry("600x400")

        # ===== FRAME PRINCIPAL =====
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # ===== FRAME LISTA =====
        frame_lista = tk.LabelFrame(main_frame, text="Eventos Programados")
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # TreeView
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # ===== FRAME ENTRADA =====
        frame_entrada = tk.LabelFrame(main_frame, text="Agregar Evento")
        frame_entrada.pack(fill=tk.X, padx=5, pady=5)

        # Fecha
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, date_pattern="yyyy-mm-dd")
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        # Descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # ===== FRAME BOTONES =====
        frame_botones = tk.Frame(main_frame)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=10)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=10)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=10)

    # ===== FUNCIONES =====
    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

            # Limpiar campos
            self.hora_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")

    def eliminar_evento(self):
        selected = self.tree.selection()
        if selected:
            confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?")
            if confirmar:
                self.tree.delete(selected)
        else:
            messagebox.showwarning("Error", "Selecciona un evento")

# ===== EJECUCIÓN =====
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista interna de tareas (texto, estado)
        self.tasks = []

        # =========================
        # INTERFAZ GRÁFICA
        # =========================
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.entry = tk.Entry(self.frame, width=40)
        self.entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        self.complete_button = tk.Button(self.frame, text="Completar", command=self.complete_task)
        self.complete_button.grid(row=1, column=0, pady=5)

        self.delete_button = tk.Button(self.frame, text="Eliminar", command=self.delete_task)
        self.delete_button.grid(row=1, column=1, pady=5)

        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # =========================
        # ATAJOS DE TECLADO
        # =========================
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<C>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    # =========================
    # FUNCIONALIDADES
    # =========================
    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")
            return

        self.tasks.append((task_text, False))  # False = pendiente
        self.entry.delete(0, tk.END)
        self.update_listbox()

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task_text, status = self.tasks[index]
            self.tasks[index] = (task_text, True)  # True = completada
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for i, (task, completed) in enumerate(self.tasks):
            if completed:
                self.listbox.insert(tk.END, f"[✔] {task}")
                self.listbox.itemconfig(i, fg="gray")
            else:
                self.listbox.insert(tk.END, f"[ ] {task}")
                self.listbox.itemconfig(i, fg="black")


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
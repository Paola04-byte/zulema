# =========================
# Clase Libro
# =========================
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # tupla (inmutable)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.info[0]} - {self.info[1]} | Categoria: {self.categoria} | ISBN: {self.isbn} | {estado}"


# =========================
# Clase Usuario
# =========================
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.libros_prestados:
                print(libro)


# =========================
# Clase Biblioteca
# =========================
class Biblioteca:
    def __init__(self):
        self.libros = {}  # diccionario ISBN : libro
        self.usuarios = {}
        self.ids_usuarios = set()  # conjunto

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro agregado.")
        else:
            print("El libro ya existe.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print("Usuario registrado.")
        else:
            print("ID ya registrado.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:

            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if not libro.prestado:
                libro.prestado = True
                usuario.prestar_libro(libro)
                print("Libro prestado correctamente.")
            else:
                print("El libro ya está prestado.")

        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:

            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro in usuario.libros_prestados:
                libro.prestado = False
                usuario.devolver_libro(libro)
                print("Libro devuelto.")
            else:
                print("Ese usuario no tiene ese libro.")

        else:
            print("Libro o usuario no encontrado.")

    def buscar_libro(self, criterio, valor):

        for libro in self.libros.values():

            if criterio == "titulo" and valor.lower() in libro.obtener_titulo().lower():
                print(libro)

            elif criterio == "autor" and valor.lower() in libro.obtener_autor().lower():
                print(libro)

            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                print(libro)


# =========================
# MENÚ DEL SISTEMA
# =========================

biblioteca = Biblioteca()

while True:

    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Ver libros prestados de un usuario")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")
        isbn = input("ISBN: ")

        libro = Libro(titulo, autor, categoria, isbn)
        biblioteca.agregar_libro(libro)

    elif opcion == "2":
        isbn = input("ISBN del libro a eliminar: ")
        biblioteca.eliminar_libro(isbn)

    elif opcion == "3":
        nombre = input("Nombre del usuario: ")
        id_usuario = int(input("ID del usuario: "))

        usuario = Usuario(nombre, id_usuario)
        biblioteca.registrar_usuario(usuario)

    elif opcion == "4":
        id_usuario = int(input("ID del usuario a eliminar: "))
        biblioteca.eliminar_usuario(id_usuario)

    elif opcion == "5":
        isbn = input("ISBN del libro: ")
        id_usuario = int(input("ID del usuario: "))
        biblioteca.prestar_libro(isbn, id_usuario)

    elif opcion == "6":
        isbn = input("ISBN del libro: ")
        id_usuario = int(input("ID del usuario: "))
        biblioteca.devolver_libro(isbn, id_usuario)

    elif opcion == "7":
        print("Buscar por: titulo / autor / categoria")
        criterio = input("Criterio: ")
        valor = input("Valor de búsqueda: ")

        biblioteca.buscar_libro(criterio, valor)

    elif opcion == "8":
        id_usuario = int(input("ID del usuario: "))
        if id_usuario in biblioteca.usuarios:
            biblioteca.usuarios[id_usuario].listar_libros()
        else:
            print("Usuario no encontrado.")

    elif opcion == "9":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
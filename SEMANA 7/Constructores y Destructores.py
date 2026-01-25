class Archivo:
    """
    Clase que representa el manejo de un archivo.
    Se utiliza para demostrar el uso del constructor y el destructor.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor:
        Se ejecuta automáticamente cuando se crea un objeto de la clase.
        Inicializa los atributos y abre el archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir contenido dentro del archivo.
        """
        self.archivo.write(texto + "\n")

    def __del__(self):
        """
        Destructor:
        Se ejecuta automáticamente cuando el objeto es eliminado
        o el programa finaliza. Se encarga de cerrar el archivo.
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")


# Programa principal
if __name__ == "__main__":
    # Se crea un objeto, lo que activa el constructor (__init__)
    archivo1 = Archivo("ejemplo.txt")

    archivo1.escribir("Este es un ejemplo de uso del constructor.")
    archivo1.escribir("El destructor cerrará el archivo automáticamente.")

    # Al eliminar el objeto, se activa el destructor (__del__)
    del archivo1

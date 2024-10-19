class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre          # Atributo público
        self.direccion = direccion    # Atributo público
        self.__libros = []            # Atributo privado

    def agregar_libro(self, libro):   # Método público
        self.__libros.append(libro)

    def __mostrar_libros(self):       # Método privado
        for libro in self.__libros:
            print(libro.titulo)


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre        # Atributo privado
        self.edad = edad              # Atributo público
        self.libros_prestados = []    # Atributo público

    def __prestar_libro(self, libro): # Método privado
        self.libros_prestados.append(libro)

    def mostrar_libros_prestados(self):  # Método público
        for libro in self.libros_prestados:
            print(libro.titulo)


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo         # Atributo público
        self.__autor = autor         # Atributo privado
        self.__isbn = isbn           # Atributo privado

    def __str__(self):  # Método privado
        return f"{self.titulo} por {self.__autor}"

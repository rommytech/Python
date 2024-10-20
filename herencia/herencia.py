# Clase A
class A:
    def __init__(self):
        print("Pertenezco a la clase A")

    def metodo_a(self):
        print("Método heredado de A")

# Clase B
class B:
    def __init__(self):
        print("Clase B")

    def metodo_b(self):
        print("Método heredado de B")

# Clase C que hereda de B y A
class C(B, A):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase B primero (según el orden de herencia)
    
    def metodo_c(self):
        print("Método es de C")

# Crear una instancia de C
objeto_c = C()

# Acceder a los métodos heredados de A, B y el propio de C
objeto_c.metodo_a()  # Método heredado de A
objeto_c.metodo_b()  # Método heredado de B
objeto_c.metodo_c()  # Método propio de C

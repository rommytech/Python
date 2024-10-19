import csv

class Estudiante:
    def __init__(self, nombres, apellidos, email, edad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.edad = edad

    def estudiante_save(self):
        with open('estudiantes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.nombres, self.apellidos, self.email, self.edad])

    def estudiante_enviar_correo(self):
        print("Enviar correo a " + self.email)
        print("Enviando correo....")

    @staticmethod
    def estudiante_buscar(email):
        try:
            with open('estudiantes.csv', mode='r') as file:
                reader = csv.reader(file)
                print("-" * 65)
                for row in reader:
                    if row[2] == email:
                        return Estudiante(row[0], row[1], row[2], row[3])
        except FileNotFoundError:
            print("No hay estudiantes registrados aún.\n")
        return None

def estudiante_mostrar(estudiante):
    print("Informacion Estudiante")
    print("======================")
    print("Nombres: " + estudiante.nombres)
    print("Apellidos: " + estudiante.apellidos)
    print("Email: " + estudiante.email)
    print("Edad: " + estudiante.edad)

def estudiante_listar():
    try:
        with open('estudiantes.csv', mode='r') as file:
            reader = csv.reader(file)
            print("-" * 65)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No hay estudiantes registrados aún.\n")
    print("+"*35)
    print(" "*35)

def menu():
    while True:
        print("1. Registrar nuevo estudiante")
        print("2. Listar estudiantes")
        print("3. Enviar correo")
        print("4. Buscar estudiante")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombres = input("Ingrese los nombres: ")
            apellidos = input("Ingrese los apellidos: ")
            email = input("Ingrese el email: ")
            edad = input("Ingrese la edad: ")

            estudiante = Estudiante(nombres, apellidos, email, edad)
            if estudiante_is_valid(nombres, apellidos, email, edad):
                estudiante.estudiante_save()
                print("Estudiante registrado exitosamente.\n")
            else:
                print("             -x- Existe datos inválidos.             -x- \n")
        
        elif opcion == '2':
            estudiante_listar()

        elif opcion == '3':
            email_a_buscar = input("Buscar correo: ")
            estudiante_encontrado = Estudiante.estudiante_buscar(email_a_buscar)
            if estudiante_encontrado:
                estudiante_encontrado.estudiante_enviar_correo()
            else:
                print("Estudiante no encontrado.\n")

        elif opcion == '4':
            email_a_buscar = input("Buscar correo: ")
            estudiante_encontrado = Estudiante.estudiante_buscar(email_a_buscar)
            if estudiante_encontrado:
                estudiante_mostrar(estudiante_encontrado)
            else:
                print("Estudiante no encontrado.\n")

        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.\n")

def estudiante_is_valid(nombres, apellidos, email, edad):
    if len(nombres.strip()) <= 0:
        return False
    if len(apellidos.strip()) <= 0:
        return False
    if len(email.strip()) <= 0:
        return False
    
    edad_tmp = 0
    try:
        edad_tmp = int(edad)
    except Exception as e:
        return False
    if edad_tmp <= 0:
        return False
    return True

# Iniciar el menú
menu()

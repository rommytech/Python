# Integers
print(isinstance(42, int))  # True
cantidad = 45
print(isinstance(cantidad, int))  # True

# Strings
nombre = "Alex"
print(isinstance(nombre, str))  # True
print(isinstance("56", int))  # False, porque "56" es un string, no un entero
print(isinstance(str(56), str))  # True, se está convirtiendo el entero 56 a string

# Números flotantes
print(isinstance(45 / 2.3, int))  # False, el resultado es un número flotante (float), no un entero

# Función mistery(), asumiendo que mistery() devuelve un valor tipo string
# Estas líneas solo funcionarán si tienes una función mistery() definida, 
# de lo contrario, arrojarán un error
# print(isinstance(mistery(), int))  # Dependerá de la definición de la función
# print(isinstance(mistery(), str))  # Dependerá de la definición de la función

# Clases
class MySuperStr(str):
    def __init__(self, valor):
        super().__init__()

texto = MySuperStr("Hola")
print(isinstance(texto, str))  # True, porque MySuperStr hereda de str
print(isinstance(texto, MySuperStr))  # True, es una instancia de MySuperStr

# Otra prueba con strings
hola = "texto"
print(isinstance(hola, str))  # True
print(isinstance(hola, str)) #True

#-----------------
class Persona:
    pass 

class Estudiante(Persona):
    pass
ipersona = Persona()
iestudiante = Estudiante()

isinstance(ipersona, Persona) #True
isinstance(ipersona, Estudiante) #False

isinstance(iestudiante, Persona) #True
isinstance(iestudiante, Estudiante) #True



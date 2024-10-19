import os

# Nombre del archivo a gestionar
nombre_archivo = "informacion.dat"

# Función para leer y mostrar el contenido del archivo
def leer_contenido_archivo():
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print(contenido)

# Comprobar si el archivo ya existe
if os.path.exists(nombre_archivo):
    print(f"El archivo '{nombre_archivo}' ya existe, ha sido creado previamente.")
    leer_contenido_archivo()  # Llamada a la función para leer el contenido
else:
    # Crear y escribir en el archivo si no existe
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Datos de información en la línea 1\n")
        archivo.write("Datos de información en la línea 2\n")
        archivo.write("Datos de información en la línea 3\n")
        archivo.write("Datos de información en la línea 4\n")
        archivo.write("Datos de información en la línea 5\n")
    
    print(f"El archivo '{nombre_archivo}' ha sido creado con éxito.")

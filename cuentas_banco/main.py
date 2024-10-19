from utils import archivo_existe, crear_archivo
from utils import leer_movimientos
from utils import registrar_movimiento
from utils import eliminar_archivo

# import es posible por el archivo __init__.py
#from nombre_archivo import nombre_funcion


print("CUENTAS DE BANCO")
print("=================")
rut = input("Ingrese RUT: ")

# Verificar si el cliente ya existe
#Si existe preguntamos qué operación

#Si no existe
#Creamos un archivo con el RUT del usuario

if archivo_existe(rut + ".csv"):
    print("Archivo ya registrado")
    #No crear archivo
    pass
else:
    crear_archivo(rut + ".csv") #Borrar luego

    print("1.- Ingresar dinero")
    print("2.- Retirar dinero")
    print("3.- Ver Movimientos")
    print("4.- Eliminar Cuenta")

opcion = input("Seleccione una opcion: ")
if opcion == "1":
    registrar_movimiento(rut + ".csv", "INGRESO", 343, 34344)
elif opcion == "2":
    registrar_movimiento(rut + ".csv", "SALIDA", 333, 34344)
elif opcion == "3":
    #Llamar a leer_movimientos
    leer_movimientos(rut + ".csv")
elif opcion == "4":
    eliminar_archivo(rut + ".csv")


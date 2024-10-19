import os
import csv

DIRECTORIO_CUENTAS = "cuentas"

def archivo_existe(nombre_archivo):
    ruta = os.path.join(DIRECTORIO_CUENTAS, nombre_archivo)
    existe = os.path.exists(ruta)
    #existe será True, cuando el archivo ya fue creado
    #existe será False, caso contrario
    return existe #Boolean

def crear_archivo(nombre_archivo):
    print("Creando archivo...")
    ruta = os.path.join(DIRECTORIO_CUENTAS, nombre_archivo)
    print("+++++++", ruta)
    with open(ruta, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Movimiento", "Valor", "Total final"])
    print("Cuenta creada")

def leer_movimientos(nombre_archivo):
    ruta = os.path.join(DIRECTORIO_CUENTAS, nombre_archivo)
    with open(ruta, mode="r") as archivo:
        lector = csv.reader(archivo)
        movimientos = list(lector)
    
    for mov in movimientos:
        print(mov)
    
def registrar_movimiento(nombre_archivo, mov, valor, total):
    ruta = os.path.join(DIRECTORIO_CUENTAS, nombre_archivo)
    with open(ruta, mode="a", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([mov, valor, total])
    print("Movimiento registrado.")
    print("Retire su tarjeta y voucher.")


def eliminar_archivo(nombre_archivo):
    ruta = os.path.join(DIRECTORIO_CUENTAS, nombre_archivo)

    existe = archivo_existe(nombre_archivo)
    if existe:
        # Puedo eliminar
        if input("¿Estás seguro? S/N: ").upper() == 'S':
            os.remove(ruta)  # Aquí debes usar la ruta completa
            print("Cuenta eliminada.")
    else:
        # Posible error
        print("¡¡Alerta!! El archivo no existe.")

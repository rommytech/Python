import csv
import os

CSV_FILE = 'planilla.csv'
FIELDNAMES = ['RUT', 'Nombres', 'Apellidos', 'Puesto', 'Sueldo', 'Se_pago']

def obtener_datos():
    """
        Args: 
        No recibe ningún argumento. 
        Returns: 
        Lista de empleados.
    """
    empleados = []
    if not os.path.exists(CSV_FILE):
        return empleados
    
    with open(CSV_FILE, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            empleados.append(row)
    return empleados

def actualizar_sueldo(rut, nuevo_sueldo):
    """
        Args:
            rut (str): EL RUT
            nuevo_sueldo: El nuevo sueldo
    """
    empleados = obtener_datos()
    updated = False
    for empleado in empleados:
        if empleado['RUT'] == rut:
            empleado['Sueldo'] = str(nuevo_sueldo)
            updated = True
            break
    
    if updated:
        escribir_csv(empleados)
        print(f"Sueldo actualizado para el empleado con RUT {rut}")
    else:
        print(f"No se encontró un empleado con el RUT {rut}")

def marcar_sueldo_pagado(rut):
    empleados = obtener_datos()
    updated = False
    for empleado in empleados:
        if empleado['RUT'] == rut:
            empleado['Se_pago'] = 'SI'
            updated = True
            break
    
    if updated:
        escribir_csv(empleados)
        print(f"Sueldo marcado como pagado para el empleado con RUT {rut}")
    else:
        print(f"No se encontró un empleado con el RUT {rut}")

def registrar_empleado():
    rut = input("Ingrese el RUT del empleado: ")
    nombres = input("Ingrese los nombres del empleado: ")
    apellidos = input("Ingrese los apellidos del empleado: ")
    puesto = input("Ingrese el puesto del empleado: ")
    sueldo = input("Ingrese el sueldo del empleado: ")
    
    nuevo_empleado = {
        'RUT': rut,
        'Nombres': nombres,
        'Apellidos': apellidos,
        'Puesto': puesto,
        'Sueldo': sueldo,
        'Se_pago': 'NO'
    }
    
    empleados = obtener_datos()
    empleados.append(nuevo_empleado)
    escribir_csv(empleados)
    print("Nuevo empleado registrado exitosamente.")

def escribir_csv(empleados):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for empleado in empleados:
            writer.writerow(empleado)


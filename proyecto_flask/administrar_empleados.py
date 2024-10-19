from planilla import obtener_datos, actualizar_sueldo, \
marcar_sueldo_pagado, registrar_empleado

def obtener_n_empleados():
    empls = obtener_datos()  # Llama a la función 'obtener_datos' para obtener la lista de empleados.
    return len(empls)  # Devuelve el número de empleados en esa lista usando 'len()'.

def mostrar_datos_empleados():
    empleados = obtener_datos()
    if empleados:
        print("Datos de los empleados:")
        for empleado in empleados:
            print(f"RUT: {empleado['RUT']}, Nombres: {empleado['Nombres']}, Apellidos: {empleado['Apellidos']}, Puesto: {empleado['Puesto']}, Sueldo: ${empleado['Sueldo']}, Se pagó: {empleado['Se_pago']}")
    else:
        print("No hay empleados registrados en la planilla.")

# Bucle principal del menú
while True:
    print("\nGESTIÓN DE SUELDOS")
    print("-------------------")
    opcion = input('''Seleccione: 
        A. Obtener datos de los empleados. 
        B. Actualizar sueldo.
        C. Marcar sueldo pagado. 
        D. Registrar un nuevo empleado.
        E. Buscar empleado por RUT.
        F. Contar el número de empleados.
        G. Salir
        >>> ''').upper()

    if opcion == 'A':
        mostrar_datos_empleados()
    elif opcion == 'B':
        rut = input("Ingrese el RUT del empleado para actualizar el sueldo: ")
        nuevo_sueldo = input("Ingrese el nuevo sueldo: ")
        actualizar_sueldo(rut, nuevo_sueldo)
    elif opcion == 'C':
        rut = input("Ingrese el RUT del empleado para marcar el sueldo como pagado: ")
        marcar_sueldo_pagado(rut)
    elif opcion == 'D':
        registrar_empleado()
    elif opcion == 'E':
        rut = input("Ingrese el RUT del empleado a buscar: ")
        buscar_empleado_por_rut(rut)
    elif opcion == 'F':
         n_empleados = obtener_n_empleados()  # Llamas a la función y guardas el resultado en 'n_empleados'
         print(f"El número total de empleados es: {n_empleados}")  # Imprimes el número de empleados
    elif opcion == 'G':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

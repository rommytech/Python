def reemplazar_informacion():
    # Abrimos el archivo en modo lectura para leer su contenido actual
    with open("informacion.dat", "r") as archivo:
        contenido = archivo.readlines()  # Leemos todas las líneas en una lista

    # Inicializamos variables para contar los reemplazos
    nuevo_contenido = []
    reemplazos = 0

    # Recorremos cada línea del archivo
    for linea in contenido:
        # Si "Información" aparece en la línea, la reemplazamos por "Procesamiento"
        if "Información" in linea:
            nueva_linea = linea.replace("Información", "Procesamiento")
            reemplazos += linea.count("Información")  # Contamos los reemplazos
        else:
            nueva_linea = linea
        
        # Agregamos la línea modificada (o la original si no hubo cambios) al nuevo contenido
        nuevo_contenido.append(nueva_linea)

    # Agregar las nuevas líneas al final del archivo (si no están ya presentes)
    nuevas_lineas = [
        "Hola Mundo\n",
        "Este en una nueva línea en el archivo\n",
        "agregando la segunda línea del archivo\n",
        "finalizando la línea agregada\n"
    ]
    
    for nueva_linea in nuevas_lineas:
        if nueva_linea not in nuevo_contenido:  # Evitar duplicados
            nuevo_contenido.append(nueva_linea)

    # Escribimos todo el contenido de nuevo en el archivo
    with open("informacion.dat", "w") as archivo:
        archivo.writelines(nuevo_contenido)

    # Imprimimos el número de reemplazos realizados
    print(f"Se realizaron {reemplazos} reemplazos")


# Llamar a la función para ejecutar el reemplazo
reemplazar_informacion()

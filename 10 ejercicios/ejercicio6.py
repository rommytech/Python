#Promedio de una lista: Solicita al usuario ingresar varios números en una lista y calcula el promedio. [5, 4, 3, 20, 21] (No use la función sum)
# Pedir al usuario que ingrese los números separados por espacios
numeros = input("Ingrese varios números separados por espacios: ").split()

# Convertir los valores ingresados en una lista de enteros
numeros = [int(x) for x in numeros]

# Inicializar variables para la suma y el contador
suma_total = 0
contador = 0

# Recorrer la lista y sumar cada elemento
for numero in numeros:
    suma_total += numero
    contador += 1

# Calcular el promedio
promedio = suma_total / contador

# Imprimir el promedio
print(f"El promedio de los números ingresados es: {promedio}")

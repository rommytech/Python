#Suma de elementos: Crea una lista de números y escribe un programa que calcule la suma de sus elementos: [5, 6, 6, 20, 12].  (No use la función sum) 
# Crear la lista de números
numeros = [5, 6, 6, 20, 12]

# Inicializar una variable para almacenar la suma
suma_total = 0

# Recorrer la lista y sumar cada elemento
for numero in numeros:
    suma_total += numero

# Imprimir la suma de los elementos
print(f"La suma de los elementos de la lista es: {suma_total}")

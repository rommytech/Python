#Sumar números impares en un rango: Del 1 al 100 Imprime todos los números impares y sumelos.
# Inicializar el acumulador para la suma de los números impares
suma_impares = 0

# Usar un bucle for para recorrer los números del 1 al 100
for numero in range(1, 101):
    # Verificar si el número es impar
    if numero % 2 != 0:
        print(numero, end=" ")  # Imprimir el número impar
        suma_impares += numero

# Imprimir la suma total de los números impares
print(f"\nLa suma de los números impares del 1 al 100 es: {suma_impares}")

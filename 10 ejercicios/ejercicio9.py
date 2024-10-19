#Sumar números pares del 1 al 100: Escribe un programa que sume los números pares entre 1 y 100 (Use for o while)
# Inicializar el acumulador para la suma de los números pares
suma_pares = 0

# Usar un bucle for para recorrer los números del 1 al 100
for numero in range(1, 101):
    # Verificar si el número es par
    if numero % 2 == 0:
        suma_pares += numero

# Imprimir la suma total de los números pares
print(f"La suma de los números pares del 1 al 100 es: {suma_pares}")

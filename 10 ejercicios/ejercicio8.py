#Contar vocales en una palabra: Solicita una palabra y cuenta cuántas vocales contiene (Palabra:  Murcielago) (Use for o while)
# Solicitar una palabra al usuario
palabra = input("Ingrese una palabra: ").lower()  # Convertir la palabra a minúsculas para facilitar la comparación

# Definir las vocales
vocales = "aeiou"

# Inicializar el contador de vocales
contador_vocales = 0

# Recorrer la palabra letra por letra
for letra in palabra:
    # Verificar si la letra es una vocal
    if letra in vocales:
        contador_vocales += 1

# Imprimir el número de vocales
print(f"La palabra '{palabra}' contiene {contador_vocales} vocales.")

#Eliminar duplicados: Dada una lista con elementos repetidos, elimina los duplicados y muestra la lista. [3, 4, 5, 5, 3, 4, 6, 7, 5]   (No use set, unset)
# Lista con elementos repetidos
numeros = [3, 4, 5, 5, 3, 4, 6, 7, 5]

# Lista vacía para almacenar los elementos sin duplicados
sin_duplicados = []

# Recorrer la lista original
for numero in numeros:
    # Si el número no está en la lista sin duplicados, agregarlo
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

# Imprimir la lista sin duplicados
print("Lista sin duplicados:", sin_duplicados)

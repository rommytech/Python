# El tesoro del pirata

# Un pirata enterró su tesoro en una isla misteriosa. Dejó un acertijo:
# "El oro está enterrado en el lugar donde la distancia entre dos árboles es exactamente 15.5 metros".
# Si la distancia es un número entero, el lugar está maldito y el tesoro desaparecerá.

# Instrucciones:
# Escribe un programa que tome como entrada la distancia entre dos árboles.
# Si la distancia es 15.5 metros, imprime "¡Tesoro encontrado!".
# Si la distancia es un número entero, imprime "¡Cuidado, es una trampa!".
# De lo contrario, imprime "Sigue buscando...".

# Lista de pares de posiciones de árboles
arboles = [
    [75123, 75107],
    [87654, 87638],
    [34567, 34550],
    [9876.5, 98749],
    [12345, 12329],
    [56789.3, 56773.1],
    [65432, 65416],
    [43210, 43194],
    [76543, 76527],
    [23047, 23031.5],
    [21098.1, 2108.2],
    [87654, 87638],
    [3456.7, 34550],
    [98765, 9874.9],
    [1234.5, 12329]
]

for distancias in arboles: 
    arbolA = distancias[0]
    arbolB = distancias[1]
    diferencia = arbolA - arbolB
    diferencia = abs(diferencia) #Retornar el valor absoluto
    print(diferencia)

    if diferencia == 15.5:
        print("¡Tesoro encontrado!")
        break  # Detenemos el bucle porque hemos encontrado el tesoro
    elif diferencia.is_integer():
        print("¡Cuidado, es una trampa!")
    else:
        print("Sigue buscando...")

def tesoro_del_pirata(arboles):
    for par in arboles:
        distancia = abs(par[0] - par[1])
        if distancia == 15.5:
            print("¡Tesoro encontrado!")
            break  # Detenemos el bucle porque hemos encontrado el tesoro
        elif distancia.is_integer():
            print("¡Cuidado, es una trampa!")
        else:
            print("Sigue buscando...")

# Ejecutamos la función
tesoro_del_pirata(arboles)

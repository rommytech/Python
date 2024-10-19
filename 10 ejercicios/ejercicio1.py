#Escribe un programa que pida un número y determine si es positivo, negativo o cero
# Pedir al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Determinar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


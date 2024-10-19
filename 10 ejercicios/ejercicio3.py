#Categoría de temperatura: Solicita una temperatura y muestra si es "Frío" (< 15°C), "Templado" (15°C - 30°C) o "Caliente" (> 30°C).
# Pedir la temperatura al usuario
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

# Determinar la categoría de la temperatura
if temperatura < 15:
    print("La temperatura es Frío.")
elif 15 <= temperatura <= 30:
    print("La temperatura es Templado.")
else:
    print("La temperatura es Caliente.")


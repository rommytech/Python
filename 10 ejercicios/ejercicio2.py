# Solicita la edad del usuario y determina si puede votar (mayor de 18 años)
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted puede votar.")
else:
    print("Usted no puede votar.")

num1 = 5
num2 = 7

print(num1 * num2)
print (num1 + num2)
print (num1 - num2)
print (num1 / num2)
print (num1 // num2)
print (num1 % num2)

# Variables Globales, cuando no hay espacios a la izquierda
# globales para main.py
num1 = 20
print("Variable modificada", num1 * num2)
if num1 > 15:
    num1 = 500
print("Variable modificada #2: ", num1 * num2)
def cambio_valor():
    """Function printing python version."""
    print("La función cambio_valor, se ejecutó")

num1 = 5
cambio_valor() #Llamar a la función
print("Variable modificada #3: ", num1 * num2)


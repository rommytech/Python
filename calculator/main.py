# Run `python main.py` in the terminal

# Note: Python is lazy loaded so the first run will take a moment,
# But after cached, subsequent loads are super fast! ⚡️
from div_utils import dividir
from sum_utils import sumar
from mul_utils import multiplicar
from rest_utils import restar
from file_utils import guardar_en_csv

def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def obtener_numeros():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    return a, b

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1/2/3/4/5): ")
    resultado = None
    if opcion == '1':
        a, b = obtener_numeros()
        resultado = sumar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '2':
        a, b = obtener_numeros()
        resultado = restar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '3':
        a, b = obtener_numeros()
        resultado = multiplicar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '4':
        a, b = obtener_numeros()
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor elige nuevamente.")

    if resultado is not None:
      if input("Desea guardar el resultado (S/N)? ").upper() == "S":
        guardar_en_csv(resultado)
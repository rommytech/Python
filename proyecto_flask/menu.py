import requests

print("Administrar Guerreros Z")
print("=======================")

def mostrar_menu():
    print("A -> Guardar en CSV todos los guerreros.")
    print("B -> Guardar en CSV a los Sayans.")
    print("C -> Guardar en CSV Enemigos de los Sayans.")
    print("D -> Salir y teletransportarse.")

def escribir_csv(nombre_archivo, data):
    import csv

    with open(nombre_archivo, mode = "a", newline = "") as archivo:
        escritor = csv.writer(archivo)
        #escritor.writerow(["Dato 1", "Dato 2", "Dato 3"])
        escritor.writerow(data)

opcion = ""
while opcion != "D":
    mostrar_menu()
    opcion = input("Por favor ingrese la opción: ")
    opcion = opcion.upper()

    if opcion == "A":
        print("Guardaré a todos los guerreros")
        #
        # Obtener información del aPI Fuente de datos Dragonball
        #
        respuesta = requests.get("https://dragonball-api.com/api/characters")
        lista_guerreros = respuesta.json()
        for guerrero in lista_guerreros["items"]:
            escribir_csv("guerreros.csv", [guerrero["name"],
                guerrero["race"], guerrero["ki"]])

    elif opcion == "B":
        print("Guardaré a los Sayans")
        respuesta = requests.get("https://dragonball-api.com/api/characters")
        lista_guerreros = respuesta.json()

        for guerrero in lista_guerreros["items"]:
            if guerrero["race"] == "Saiyan":
                escribir_csv("sayans.csv", [guerrero["name"], guerrero["ki"]])
                
    elif opcion == "C":
        print("Guardaré a los Enemigos de los Sayans")
        respuesta = requests.get("https://dragonball-api.com/api/characters")
        lista_guerreros = respuesta.json()

        for guerrero in lista_guerreros["items"]:
            if guerrero["race"] != "Saiyan":
                escribir_csv("enemigos_sayans.csv", [guerrero["name"], guerrero["race"], guerrero["ki"]])

    elif opcion == "D":
        print("Saliendo y teletransportándose... Adiós!")
    else:
        print("Por favor, elige A, B, C o D.")

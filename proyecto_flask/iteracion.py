nombres= [
    "Leo", "Carlos", "Segundo", "Nicolás"
]

#While
contador = 0 
while len(nombres) > contador:
    print(nombres[contador])
    contador += 1 #Incrementa en 1

#For
for item in nombres:
    print(item)

frutas = ["Naranja", "Manzana", "Piña", "Plátano", "Uva", "Sandía"]
for item in frutas:
    print(item)

estadisticas = [
    [1212, 2323], 
    [233, 232], 
    [23234, 343]
    ]
for par in estadisticas:
    print("A:" + str(par[0]) + " B: " + str(par[1]))
    suma = par[0] + par[1]
    print(suma)
    print("---")
    #Algoritmo para enviar por correo a la par

superheroes = [{
    "nombre": "Spiderman",
    "poder": "Telaraña",
    "edad": 23
}, {
    "nombre": "Batman",
    "poder": "Murciélago",
    "edad": 39
}, {
    "nombre": "Deadpool",
    "poder": "Cuarta dimensión",
    "edad": 40
}]

for hero in superheroes:
    print("El poder de " + hero ["nombre"] + " es " + hero["poder"])

# Lista de personas con diferentes características
personas = [
    {"edad": 34, "peso": 40,},   # Puede pasar (edad > 18 y peso <= 70.5)
    {"edad": 16, "peso": 71,},   # No puede pasar (edad <= 18)
    {"edad": 17, "peso": 72,},   # No puede pasar (peso > 70.5)
    {"edad": 17, "peso": 50,},   # Error de Sistema. Puede pasar (peso == 50)
    {"edad": 34, "peso": 40,},   # Puede pasar (edad > 18 y peso <= 70.5)
]

def robot_guardian():
    for persona in personas:
        if persona["edad"] > 18 and persona["peso"] <= 70.5:
            print("Puede pasar.")
        elif persona["peso"] == 50:
            print("Error de Sistema. Puede pasar.")
        else:
            print("No puede pasar.")

# Ejecutamos la función
robot_guardian()

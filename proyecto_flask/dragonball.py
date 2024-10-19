import requests

print("DRAGON BALL")
print("-----------")

respuesta = requests.get("https://dragonball-api.com/api/characters")
# respuesta es un objeto tipo HTTP
datos = respuesta.json() #Convierte la data en JSON
# datos: JSON =>
n_sayans = 0
n_males = 0
n_females = 0
n_namekians = 0
n_high_ki = 0
razas = set()  

for guerrero in datos["items"]:
    print(guerrero["name"])
    
    # Contar Sayans
    if guerrero.get("race") == "Saiyan": 
        n_sayans += 1
    
    # Contar masculinos
    if guerrero.get("gender") == "Male":
        n_males += 1
    
    # Contar femeninos
    if guerrero.get("gender") == "Female":
        n_females += 1
    
    # Contar Namekians
    if guerrero.get("race") == "Namekian":
        n_namekians += 1
    
    # Contar personajes con Ki > 2,000,000
    ki_value = guerrero.get("ki", "0").replace(".", "")
    if int(ki_value) > 2000000:
        n_high_ki += 1
    
    # Agregar raza 
    if guerrero.get("race"):
        razas.add(guerrero["race"])

print("Número de Sayans: ", n_sayans)
print("Número de Masculinos: ", n_males)
print("Número de Femeninos: ", n_females)
print("Número de Namekians: ", n_namekians)
print("Número de personajes con Ki mayor a 2.000.000: ", n_high_ki)
print("Número de razas diferentes: ", len(razas))

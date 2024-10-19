print("Listas: ")
estudiantes = ["Andrés", "Constanza", "Luis"]
# estudiantes es una lista o array u objetos de información

estudiante = {
    "nombre": "Andrés",
    "apellido": "Fuentes",
    "especialidad": "Ingeniero",
    "hobbies": ["correr", "bailar", "saltar"]
}
# estudiante es un diccionario

estudiantes_detalle = [{
    "nombre": "Andrés",
    "apellido": "Fuentes"
}, {
    "nombre": "Claudia",
    "apellido": "Onate"
}]
print("Hobbie bailar: ", estudiante["hobbies"][1])
print("Apellido Claudia:", estudiantes_detalle[1]["apellido"])


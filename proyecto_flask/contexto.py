nombre =  "Leo"
apellido = "Rojas"

def cambiar_nombre():
    nombre = "Ray" #Local
    print("Se cambió el nombre !!!")
    print("El nombre local es: " + nombre)
    print("El apellido global es: " + apellido)

cambiar_nombre()

print("El nombre es: " + nombre)

# python contexto.py

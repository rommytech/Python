from postulante import Postulante

print("Formulario Registro Especialidades")
print("==================================")

nombres = input("Ingrese nombres completos: ")
egreso = input("Año de egreso: ")
especialidad = input("Ingrese la especialidad que desea: ")

post = Postulante(nombres, egreso, especialidad)
if post.is_valid():
    post.save()
    print("¡Guardado!")
else:
    print("Error")  
# Llamamos al método correctamente con paréntesis

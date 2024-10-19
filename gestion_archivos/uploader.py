import requests

ruta = "archivos_varios/file1.png"

with open(ruta, mode="rb") as mi_mejor_foto:
    # Tengo el archivo abierto de forma binaria
    respuesta = requests.post("https://file.io", files={"file": mi_mejor_foto})
    
    if respuesta.status_code == 200:
        print("Archivo subido!!")
        print(respuesta.json()["link"])
    else:
        print("Error al subir archivo")

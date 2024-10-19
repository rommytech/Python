import os

pdfs = []
imagenes_png = []
imagenes_jpeg = []
imagenes_jpg = []
imagenes_gif = []
docxs = []

for archivo in os.listdir("archivos_varios"):
    if archivo.endswith(".pdf"):
        pdfs.append(archivo)  # Incluir el archivo en la lista de pdfs
    elif archivo.endswith(".docx"):
        docxs.append(archivo)  # Incluir el archivo en la lista de docx
    elif archivo.endswith(".png"):
        imagenes_png.append(archivo)  # Incluir en la lista de imágenes PNG
    elif archivo.endswith(".jpeg"):
        imagenes_jpeg.append(archivo)  # Incluir en la lista de imágenes JPEG
    elif archivo.endswith(".jpg"):
        imagenes_jpg.append(archivo)  # Incluir en la lista de imágenes JPG
    elif archivo.endswith(".gif"):
        imagenes_gif.append(archivo)  # Incluir en la lista de imágenes GIF

print("Pdfs encontrados: " + str(len(pdfs)))
print("Docx encontrados: " + str(len(docxs)))
print("Imágenes PNG encontradas: " + str(len(imagenes_png)))
print("Imágenes JPEG encontradas: " + str(len(imagenes_jpeg)))
print("Imágenes JPG encontradas: " + str(len(imagenes_jpg)))
print("Imágenes GIF encontradas: " + str(len(imagenes_gif)))
  
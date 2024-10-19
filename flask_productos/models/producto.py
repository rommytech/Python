import csv
import os

class Producto:
    def __init__(self, nombre, precio, descripcion):
        # Completa la definición del constructor
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def is_valid(self):
        # Validar que el nombre tenga al menos 3 caracteres
        # Validar que el precio sea mayor o igual a 1
        # Validar que la descripción tenga al menos 3 caracteres
        if len(self.nombre) < 3:
            return False
        if not isinstance(self.precio, (int, float)) or self.precio < 1:
            return False
        if len(self.descripcion) < 3:
            return False
        return True

    def save(self):
        # Guardar el producto en un archivo CSV
        file_path = 'productos.csv'
        with open(file_path, 'a', newline='') as csvfile:
            fieldnames = ['nombre', 'precio', 'descripcion']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Escribir los datos del producto
            writer.writerow({
                'nombre': self.nombre,
                'precio': self.precio,
                'descripcion': self.descripcion
            })

    @staticmethod
    def contar_registros():
        # Contar el número de registros en el archivo CSV
        file_path = 'productos.csv'
        if not os.path.exists(file_path):
            return 0
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return sum(1 for row in reader)  # Contar las filas del CSV
